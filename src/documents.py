from typing import List

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.config import DATA_DIR


def load_documents() -> List[Document]:
    """Carga documentos Markdown y TXT desde la carpeta data/."""
    paths = sorted(
        list(DATA_DIR.glob("*.md"))
        + list(DATA_DIR.glob("*.txt"))
    )

    documents = []

    for path in paths:
        text = path.read_text(encoding="utf-8").strip()

        if not text:
            continue

        documents.append(
            Document(
                page_content=text,
                metadata={
                    "source": path.name,
                    "page": 1,
                    "category": path.stem.split("_")[0].lower(),
                },
            )
        )

    if not documents:
        raise ValueError(
            "No se encontraron documentos .md o .txt con contenido en data/."
        )

    return documents


def split_documents() -> List[Document]:
    """Divide los documentos en fragmentos con solapamiento."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=3000,
        chunk_overlap=300,
        separators=["\n## ", "\n### ", "\n\n", "\n", ". ", " ", ""],
        add_start_index=True,
    )

    chunks = splitter.split_documents(load_documents())

    for index, chunk in enumerate(chunks):
        source = chunk.metadata["source"]
        start = chunk.metadata.get("start_index", 0)

        chunk.metadata["chunk_id"] = f"{source}::chunk-{start}"
        chunk.metadata["chunk_number"] = index

    return chunks
