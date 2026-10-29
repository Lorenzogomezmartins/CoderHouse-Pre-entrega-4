# Sistema RAG escalable en la nube con Pinecone

Proyecto de la Pre-entrega 4 del curso de IA Engineering de Coderhouse.

Implementa un sistema de recuperación de información (RAG) que combina búsqueda semántica mediante embeddings almacenados en Pinecone Serverless y búsqueda léxica mediante BM25.

## Características

- **Ingesta de documentos:** procesa archivos Markdown y los divide en fragmentos mediante `RecursiveCharacterTextSplitter`.
- **Embeddings:** utiliza el modelo `gemini-embedding-001` de Google.
- **Base vectorial:** almacena los fragmentos y sus metadatos en Pinecone Serverless.
- **Recuperación híbrida:** combina resultados de BM25 con búsqueda vectorial mediante Reciprocal Rank Fusion (RRF).
- **Namespace:** organiza los documentos bajo `docs-tecnicas`.
- **Evaluación:** calcula Precision@5 y Recall@5 con cinco preguntas de prueba.

## Tecnologías

- Python
- Google Gemini API
- Pinecone Serverless
- LangChain
- BM25
- python-dotenv

## Estructura del proyecto

```text
pre-entrega-4/
├── data/
│   ├── http_status.md
│   ├── python_listas.md
│   ├── apis_rest.md
│   ├── sql_bases_datos.md
│   └── git_control_versiones.md
├── src/
│   ├── config.py
│   ├── documents.py
│   ├── embeddings.py
│   ├── setup_pinecone.py
│   ├── ingest.py
│   └── retriever.py
├── .env.example
├── .gitignore
├── evaluate.py
├── requirements.txt
└── README.md
```

## Requisitos previos

- Python instalado.
- Una API key de Google AI Studio.
- Una API key de Pinecone.

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/Lorenzogomezmartins/CoderHouse-Pre-entrega-4.git
cd CoderHouse-Pre-entrega-4
```

Crear y activar un entorno virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Instalar las dependencias:

```bash
python -m pip install -r requirements.txt
```

## Configuración

Crear un archivo `.env` en la raíz del proyecto, tomando `.env.example` como referencia.

Configurar las siguientes variables con las claves propias:

```dotenv
GOOGLE_API_KEY=tu_clave_de_google
PINECONE_API_KEY=tu_clave_de_pinecone
INDEX_NAME=pre-entrega-4-rag
GOOGLE_EMBEDDING_MODEL=gemini-embedding-001
EMBEDDING_DIMENSION=768
PINECONE_NAMESPACE=docs-tecnicas
PINECONE_CLOUD=aws
PINECONE_REGION=us-east-1
```

No subir el archivo `.env` ni publicar claves de API.

## Crear el índice e ingerir documentos

Inicializar el índice Serverless de Pinecone:

```bash
python -m src.setup_pinecone
```

Procesar los documentos, generar embeddings y almacenarlos en Pinecone:

```bash
python -m src.ingest
```

La ingesta debe ejecutarse después de crear el índice y cada vez que se necesite cargar o actualizar el conjunto de documentos.

## Ejecutar el recuperador

```bash
python -m src.retriever
```

El sistema permite ingresar consultas técnicas y devuelve los fragmentos recuperados mediante la combinación de búsqueda léxica y semántica. Para salir, escribir `salir`.

## Evaluación

Ejecutar:

```bash
python evaluate.py
```

El benchmark contiene cinco preguntas sobre códigos HTTP, listas de Python, APIs REST, claves primarias de SQL y Git.

Las métricas utilizadas son:

- **Precision@5:** proporción de documentos recuperados en el Top-5 que coinciden con el documento esperado.
- **Recall@5:** indica si el documento esperado aparece entre los cinco resultados recuperados.

### Resultados de la última ejecución

| Métrica | Resultado |
|---|---:|
| Precision@5 promedio | 20 % |
| Recall@5 promedio | 100 % |

Los resultados corresponden a la última ejecución local registrada. La evaluación considera relevante la coincidencia entre el archivo recuperado y el documento esperado.

## Autor

Lorenzo Gómez Martins

Repositorio: https://github.com/Lorenzogomezmartins/CoderHouse-Pre-entrega-4
