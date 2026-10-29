import math
from typing import List

from google import genai
from google.genai import types
from langchain_core.embeddings import Embeddings

from src.config import (
    GOOGLE_API_KEY,
    EMBEDDING_MODEL,
    EMBEDDING_DIMENSION,
    validate_google_key,
)


class GeminiEmbeddings(Embeddings):
    """Genera embeddings con Gemini para guardarlos en Pinecone."""

    def __init__(self):
        validate_google_key()
        self.client = genai.Client(api_key=GOOGLE_API_KEY)
        self.model = EMBEDDING_MODEL
        self.dimension = EMBEDDING_DIMENSION

    def _embed_batch(self, texts: List[str]) -> List[List[float]]:
        response = self.client.models.embed_content(
            model=self.model,
            contents=texts,
            config=types.EmbedContentConfig(
                output_dimensionality=self.dimension
            ),
        )

        output = []

        for item in response.embeddings:
            values = [float(value) for value in item.values]

            if len(values) != self.dimension:
                raise ValueError(
                    f"Gemini devolvió {len(values)} dimensiones, "
                    f"pero Pinecone espera {self.dimension}."
                )

            # Normalizamos los vectores para utilizar similitud coseno.
            norm = math.sqrt(sum(value * value for value in values))
            if norm:
                values = [value / norm for value in values]

            output.append(values)

        return output

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        result = []

        for start in range(0, len(texts), 16):
            batch = texts[start:start + 16]
            result.extend(self._embed_batch(batch))

        return result

    def embed_query(self, text: str) -> List[float]:
        return self._embed_batch([text])[0]
