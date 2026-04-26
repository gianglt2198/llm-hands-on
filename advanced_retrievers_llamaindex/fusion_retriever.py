print("=" * 60)
print("6. QUERY FUSION RETRIEVER - OVERVIEW")
print("=" * 60)


from llama_index.core.retrievers import QueryFusionRetriever

from retriever import lab
from docs import DEMO_QUERIES

# Create base retriever
base_retriever = lab.vector_index.as_retriever(similarity_top_k=3)

query = DEMO_QUERIES["comprehensive"]  # "What are the main approaches to machine learning?"
print(f"Query: {query}")

print("=" * 60)
print("6.1 RECIPROCAL RANK FUSION MODE DEMONSTRATION")
print("=" * 60)

# Create query fusion retriever with RRF mode
rrf_query_fusion = QueryFusionRetriever(
    [base_retriever],
    similarity_top_k=3,
    num_queries=3,
    mode="reciprocal_rerank",
    use_async=False,
    verbose=True
)

nodes = rrf_query_fusion.retrieve(query)

print(f"\nRRF Query Fusion Results:")
for i, node in enumerate(nodes, 1):
    print(f"{i}. Final RRF Score: {node.score:.4f}")
    print(f"   Text: {node.text[:100]}...")
    print()

print("=" * 60)
print("6.2 RELATIVE SCORE FUSION MODE DEMONSTRATION")
print("=" * 60)

rel_score_fusion = QueryFusionRetriever(
    [base_retriever],
    similarity_top_k=3,
    num_queries=3,
    mode="relative_score",
    use_async=False,
    verbose=False
)

nodes = rel_score_fusion.retrieve(query)

print(f"\nRelative Score Fusion Results:")
for i, node in enumerate(nodes, 1):
    print(f"{i}. Combined Relative Score: {node.score:.4f}")
    print(f"   Text: {node.text[:100]}...")
    print()

print("=" * 60)
print("6.3 DISTRIBUTION-BASED SCORE FUSION MODE DEMONSTRATION")
print("=" * 60)

dist_fusion = QueryFusionRetriever(
    [base_retriever],
    similarity_top_k=3,
    num_queries=3,
    mode="dist_based_score",
    use_async=False,
    verbose=False
)
nodes = dist_fusion.retrieve(query)

print(f"\nDistribution-Based Fusion Results:")
for i, node in enumerate(nodes, 1):
    print(f"{i}. Statistically Normalized Score: {node.score:.4f}")
    print(f"   Text: {node.text[:100]}...")
    print()