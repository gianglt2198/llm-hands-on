from llama_index.core import (
    VectorStoreIndex,
    Document,
    DocumentSummaryIndex,
    KeywordTableIndex
)

from llama_index.core.node_parser import SentenceSplitter

from docs import SAMPLE_DOCUMENTS
import models


class AdvancedRetrieversLab:
    def __init__(self):
        print("🚀 Initializing Advanced Retrievers Lab...")
        self.documents = [Document(text=text) for text in SAMPLE_DOCUMENTS]
        self.nodes = SentenceSplitter().get_nodes_from_documents(self.documents)

        print("📊 Creating indexes...")
        self.vector_index = VectorStoreIndex.from_documents(self.documents)
        self.document_summary_index = DocumentSummaryIndex.from_documents(self.documents)
        self.keyword_index = KeywordTableIndex.from_documents(self.documents)

        print("✅ Advanced Retrievers Lab Initialized!")
        print(f"📄 Loaded {len(self.documents)} documents")
        print(f"🔢 Created {len(self.nodes)} nodes")


lab = AdvancedRetrieversLab()