from langchain_classic.chains import RetrievalQA, ConversationalRetrievalChain
from langchain_core.prompts import PromptTemplate
from langchain_classic.memory import ConversationBufferMemory

from model import llm
from doc_processing import docsearch

prompt_template = """Use the information from the document to answer the question at the end. If you don't know the answer, just say that you don't know, definately do not try to make up an answer.

{context}

Question: {question}
"""

PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)

chain_type_kwargs = {"prompt": PROMPT}

memory = ConversationBufferMemory(memory_key = "chat_history", return_message = True)

qa = ConversationalRetrievalChain.from_llm(
    llm=llm,
    chain_type="stuff",
    retriever=docsearch.as_retriever(),
    # chain_type_kwargs=chain_type_kwargs, 
    memory = memory, 
    get_chat_history=lambda h : h, 
    return_source_documents=False
)

history = []

query = "What is mobile policy?"
result = qa.invoke({"question":query}, {"chat_history": history})
print(result["answer"])
history.append((query, result["answer"]))
query = "List points in it?"
result = qa.invoke({"question": query}, {"chat_history": history})
print(result["answer"])
history.append((query, result["answer"]))
query = "What is the aim of it?"
result = qa({"question": query}, {"chat_history": history})
print(result["answer"])