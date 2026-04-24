import chromadb
from chromadb.utils import embedding_functions

# Define the embedding function using SentenceTransformers
ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

client = chromadb.Client()


def create_collection(name: str, metadata: dict):
    return client.create_collection(
        name=name,
        metadata=metadata,
        configuration={
            "hnsw": {"space": "cosine"},
            "embedding_function": ef
        }
    )

