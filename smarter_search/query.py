from loader import text_data
from models.embedding import embeddings
from langchain_chroma import Chroma

vectordb = Chroma.from_documents(documents=text_data, embedding=embeddings)

query = "smoking policy"
retriever = vectordb.as_retriever(
    # search_type="mmr"
    # search_type="similarity_score_threshold", search_kwargs={"score_threshold": 0.4}
    search_kwargs={"k": 2}
)

docs = retriever.invoke(query)

print("---------- DOCS ---------")
print(docs)
