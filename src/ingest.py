from pinecone import Pinecone

from src.config import (
    PINECONE_API_KEY,
    INDEX_NAME,
    PINECONE_NAMESPACE,
    validate_pinecone_key,
)
from src.documents import split_documents
from src.embeddings import GeminiEmbeddings


def main():
    validate_pinecone_key()

    chunks = split_documents()
    embeddings = GeminiEmbeddings()

    print(f"Fragmentos preparados: {len(chunks)}")
    print("Generando embeddings con Gemini...")

    vectors = embeddings.embed_documents(
        [document.page_content for document in chunks]
    )

    pc = Pinecone(api_key=PINECONE_API_KEY)
    index = pc.Index(INDEX_NAME)

    records = []

    for document, vector in zip(chunks, vectors):
        metadata = dict(document.metadata)
        metadata["text"] = document.page_content

        records.append(
            {
                "id": metadata["chunk_id"],
                "values": vector,
                "metadata": metadata,
            }
        )

    batch_size = 100

    for start in range(0, len(records), batch_size):
        batch = records[start:start + batch_size]

        index.upsert(
            vectors=batch,
            namespace=PINECONE_NAMESPACE,
        )

        print(
            f"Subidos {min(start + batch_size, len(records))}"
            f"/{len(records)} fragmentos."
        )

    print(
        f"Ingesta terminada: {len(records)} fragmentos "
        f"en namespace '{PINECONE_NAMESPACE}'."
    )


if __name__ == "__main__":
    main()
