print("=" * 60)
print("1. VECTOR INDEX RETRIEVER")
print("=" * 60)

from llama_index.core.retrievers import (
    VectorIndexRetriever
)

from docs import DEMO_QUERIES
from retriever import lab


vector_retriever = VectorIndexRetriever(
    index = lab.vector_index,
    similarity_top_k = 3
)

alt_retriever = lab.vector_index.as_retriever(similarity_top_k=3)

query = DEMO_QUERIES["basic"]
nodes = vector_retriever.retrieve(query)

print(f"Query: {query}")
print(f"Retrieved {len(nodes)} nodes:")
for i, node in enumerate(nodes, 1):
    print(f"{i}. Score: {node.score:.4f}")
    print(f"   Text: {node.text[:100]}...")
    print()