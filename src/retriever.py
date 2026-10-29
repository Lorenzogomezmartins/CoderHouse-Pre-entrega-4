
from typing import Any, List

from pydantic import ConfigDict
from pinecone import Pinecone

from langchain_core.documents import Document
from langchain_core.retrievers import BaseRetriever
from langchain_core.callbacks import CallbackManagerForRetrieverRun
from langchain_community.retrievers import BM25Retriever

from src.config import (
    PINECONE_API_KEY,
    INDEX_NAME,
    PINECONE_NAMESPACE,
    validate_pinecone_key,
)
from src.documents import split_documents
from src.embeddings import GeminiEmbeddings


class PineconeRetriever(BaseRetriever):
    """Recupera documentos mediante similitud vectorial en Pinecone."""

    index: Any
    embeddings: Any
    namespace: str = "docs-tecnicas"
    k: int = 5

    model_config = ConfigDict(arbitrary_types_allowed=True)

    def _get_relevant_documents(
        self,
        query: str,
        *,
        run_manager: CallbackManagerForRetrieverRun,
    ) -> List[Document]:
        vector = self.embeddings.embed_query(query)

        response = self.index.query(
            vector=vector,
            top_k=self.k,
            include_metadata=True,
            namespace=self.namespace,
        )

        documents = []

        for match in response.matches:
            metadata = dict(match.metadata or {})
            text = metadata.pop("text", "")

            metadata["pinecone_score"] = float(match.score or 0)
            metadata["chunk_id"] = match.id

            documents.append(
                Document(page_content=text, metadata=metadata)
            )

        return documents


class RAGSystem:
    """Combina recuperación léxica BM25 y recuperación vectorial."""

    def __init__(self, k: int = 5):
        validate_pinecone_key()

        self.k = k
        self.embeddings = GeminiEmbeddings()

        pc = Pinecone(api_key=PINECONE_API_KEY)
        self.index = pc.Index(INDEX_NAME)

        # Corpus local para búsqueda por palabras clave.
        local_documents = split_documents()

        self.bm25 = BM25Retriever.from_documents(
            local_documents,
            k=k,
        )

        self.vector_retriever = PineconeRetriever(
            index=self.index,
            embeddings=self.embeddings,
            namespace=PINECONE_NAMESPACE,
            k=k,
        )

    @staticmethod
    def _normalize_scores(documents: List[Document]) -> dict:
        """Asigna un puntaje relativo según la posición de cada resultado."""
        scores = {}

        for rank, document in enumerate(documents):
            chunk_id = (
                document.metadata.get("chunk_id")
                or document.metadata.get("source", "")
                + ":"
                + document.page_content[:100]
            )

            # Reciprocal Rank Fusion: favorece documentos bien posicionados
            # en ambas listas, sin comparar directamente scores incompatibles.
            scores[chunk_id] = scores.get(chunk_id, 0.0) + (
                1.0 / (60 + rank + 1)
            )

        return scores

    def retrieve(self, query: str) -> List[Document]:
        """Combina BM25 y Pinecone con Reciprocal Rank Fusion (RRF)."""

        lexical_results = self.bm25.invoke(query)
        vector_results = self.vector_retriever.invoke(query)

        combined = {}
        scores = {}

        # Peso léxico: 0.4
        for rank, document in enumerate(lexical_results):
            key = (
                document.metadata.get("chunk_id")
                or document.metadata.get("source", "")
                + ":"
                + document.page_content[:100]
            )

            combined[key] = document
            scores[key] = scores.get(key, 0.0) + (
                0.4 / (60 + rank + 1)
            )

        # Peso semántico: 0.6
        for rank, document in enumerate(vector_results):
            key = (
                document.metadata.get("chunk_id")
                or document.metadata.get("source", "")
                + ":"
                + document.page_content[:100]
            )

            combined[key] = document
            scores[key] = scores.get(key, 0.0) + (
                0.6 / (60 + rank + 1)
            )

        ordered_keys = sorted(
            scores,
            key=scores.get,
            reverse=True,
        )

        return [combined[key] for key in ordered_keys[:self.k]]


if __name__ == "__main__":
    system = RAGSystem(k=5)

    while True:
        question = input(
            "\nConsulta técnica (escribí 'salir' para terminar): "
        ).strip()

        if question.lower() in {"salir", "exit", "quit"}:
            break

        if not question:
            print("Ingresá una consulta.")
            continue

        results = system.retrieve(question)

        if not results:
            print("No se encontraron documentos.")
            continue

        for position, document in enumerate(results, start=1):
            print(
                f"\n{position}. "
                f"{document.metadata.get('source', 'Sin fuente')}"
            )
            print(document.page_content[:500])
