print("=" * 60)
print("2. BM25 RETRIEVER")
print("=" * 60)

from llama_index.retrievers.bm25 import BM25Retriever

import Stemmer

from retriever import lab
from docs import DEMO_QUERIES

bm25_retriever = BM25Retriever.from_defaults(
    nodes=lab.nodes,
    similarity_top_k=3,
    stemmer=Stemmer.Stemmer("english"),
    language="english"
)

query = DEMO_QUERIES["technical"]
nodes = bm25_retriever.retrieve(query)

print(f"Query: {query}")
print("BM25 analyzes exact keyword matches with sophisticated scoring")
print(f"Retrieved {len(nodes)} nodes:")

for i, node in enumerate(nodes, 1):
    score = node.score if hasattr(node, 'score') and node.score else 0
    print(f"{i}. BM25 Score: {score:.4f}")
    print(f"   Text: {node.text[:100]}...")
    
    # Highlight which query terms appear in the text
    text_lower = node.text.lower()
    query_terms = query.lower().split()
    found_terms = [term for term in query_terms if term in text_lower]
    if found_terms:
        print(f"   → Found terms: {found_terms}")
    print()
