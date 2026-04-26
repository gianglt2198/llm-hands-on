from langchain_classic.retrievers.self_query.base import SelfQueryRetriever

from loader import vectordb, metadata_field_info
from models.model import llm

document_content_description = "Brief summary of a movie"

retriever = SelfQueryRetriever.from_llm(
    llm,
    vectordb,
    document_contents=document_content_description,
    metadata_field_info=metadata_field_info
)

# docs = retriever.invoke("I want to watch a movie rated higher than 8.5")
docs = retriever.invoke("Has Greta Gerwig directed any movies about women")
# docs = retriever.invoke("What's a highly rated (above 8.5) science fiction film?")
print("---------- DOCS ---------")
for doc in docs:
    print(doc)