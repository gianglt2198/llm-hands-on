print("=" * 60)
print("4. AUTO MERGING RETRIEVER")
print("=" * 60)


from llama_index.core import (
    VectorStoreIndex
)
from llama_index.core.retrievers import AutoMergingRetriever
from llama_index.core.node_parser import HierarchicalNodeParser


from retriever import lab
from docs import DEMO_QUERIES

node_parser = HierarchicalNodeParser.from_defaults(
    chunk_sizes=[512, 256, 128]
)

hier_nodes = node_parser.get_nodes_from_documents(lab.documents)

from llama_index.core import StorageContext 
from llama_index.core.storage.docstore import SimpleDocumentStore
from llama_index.core.vector_stores import SimpleVectorStore

docstore = SimpleDocumentStore()
docstore.add_documents(hier_nodes)

storage_context = StorageContext.from_defaults(docstore=docstore)

base_index = VectorStoreIndex(hier_nodes, storage_context=storage_context)
base_retriever = base_index.as_retriever(similarity_top_k=6)

auto_merging_retriever = AutoMergingRetriever(
    base_retriever,
    storage_context,
    verbose=True
)

query = DEMO_QUERIES["advanced"]  # "How do neural networks work in deep learning?"
nodes = auto_merging_retriever.retrieve(query)

print(f"Query: {query}")
print(f"Auto-merged to {len(nodes)} nodes")
for i, node in enumerate(nodes[:3], 1):
    print(f"{i}. Score: {node.score:.4f}" if hasattr(node, 'score') and node.score else f"{i}. (Auto-merged)")
    print(f"   Text: {node.text[:120]}...")
    print()