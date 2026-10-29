import time

from pinecone import Pinecone, ServerlessSpec

from src.config import (
    PINECONE_API_KEY,
    INDEX_NAME,
    EMBEDDING_DIMENSION,
    PINECONE_CLOUD,
    PINECONE_REGION,
    validate_pinecone_key,
)


def main():
    validate_pinecone_key()

    pc = Pinecone(api_key=PINECONE_API_KEY)
    names = pc.list_indexes().names()

    if INDEX_NAME in names:
        description = pc.describe_index(INDEX_NAME)

        if description.dimension != EMBEDDING_DIMENSION:
            raise ValueError(
                f"El índice tiene dimensión {description.dimension}, "
                f"pero la configuración exige {EMBEDDING_DIMENSION}. "
                "Usá otro INDEX_NAME o corregí la configuración."
            )

        print(
            f"El índice '{INDEX_NAME}' ya existe "
            f"con dimensión {description.dimension}."
        )
        return

    print(f"Creando índice Serverless: {INDEX_NAME}")

    pc.create_index(
        name=INDEX_NAME,
        dimension=EMBEDDING_DIMENSION,
        metric="cosine",
        spec=ServerlessSpec(
            cloud=PINECONE_CLOUD,
            region=PINECONE_REGION,
        ),
    )

    while not pc.describe_index(INDEX_NAME).status["ready"]:
        print("Esperando a que Pinecone prepare el índice...")
        time.sleep(2)

    print("Índice creado y listo para usar.")


if __name__ == "__main__":
    main()
