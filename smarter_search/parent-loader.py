from langchain_classic.retrievers.parent_document_retriever import ParentDocumentRetriever
from langchain_text_splitters import CharacterTextSplitter
from langchain_core.stores import InMemoryStore
from langchain_chroma import Chroma

from models.embedding import embeddings
from loader import text_data

parent_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=20, separator='\n')
child_splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=20, separator='\n')

vectordb = Chroma(
    collection_name="split_parents", embedding_function = embeddings
)

store = InMemoryStore()

retriever = ParentDocumentRetriever(
    vectorstore=vectordb,
    docstore=store,
    child_splitter=child_splitter,
    parent_splitter=parent_splitter,
)

retriever.add_documents(text_data)

print(len(list(store.yield_keys())))

sub_docs = vectordb.similarity_search("smoking policy")

print(sub_docs)