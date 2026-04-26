from langchain_classic.retrievers.multi_query import MultiQueryRetriever

from loader import vectordb
from models.model import llm

## PDF VECTOR DB ------------------------------------------------

query = "What does the paper say about langchain?"

retriever = MultiQueryRetriever.from_llm(
    retriever=vectordb.as_retriever(),
    llm=llm
)

docs = retriever.invoke(query)

print("---------- DOCS ---------")
print(docs)
