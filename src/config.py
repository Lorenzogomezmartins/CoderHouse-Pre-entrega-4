import os
from pathlib import Path
from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parent.parent
load_dotenv(ROOT_DIR / ".env")

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY", "")
INDEX_NAME = os.getenv("INDEX_NAME", "pre-entrega-4-rag")
EMBEDDING_MODEL = os.getenv(
    "GOOGLE_EMBEDDING_MODEL", "gemini-embedding-001"
)
EMBEDDING_DIMENSION = int(os.getenv("EMBEDDING_DIMENSION", "768"))
PINECONE_NAMESPACE = os.getenv("PINECONE_NAMESPACE", "docs-tecnicas")
PINECONE_CLOUD = os.getenv("PINECONE_CLOUD", "aws")
PINECONE_REGION = os.getenv("PINECONE_REGION", "us-east-1")
DATA_DIR = ROOT_DIR / "data"


def validate_google_key():
    if not GOOGLE_API_KEY or GOOGLE_API_KEY.startswith("TU_"):
        raise ValueError(
            "Configurá GOOGLE_API_KEY en el archivo .env."
        )


def validate_pinecone_key():
    if not PINECONE_API_KEY or PINECONE_API_KEY.startswith("TU_"):
        raise ValueError(
            "Configurá PINECONE_API_KEY en el archivo .env."
        )
