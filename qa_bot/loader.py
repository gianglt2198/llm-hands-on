from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_classic.chains import RetrievalQA

from llm import embedding_model, llm_model

def document_loader(file):
    loader = PyPDFLoader(file.name)
    loaded_document = loader.load()
    return loaded_document

## Text splitter
def text_splitter(data):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=50,
        length_function=len,
    )
    chunks = text_splitter.split_documents(data)
    return chunks

def vector_database(chunks):
    vectordb = Chroma.from_documents(chunks, embedding_model)
    return vectordb

## Retriever
def retriever(file):
    splits = document_loader(file)
    chunks = text_splitter(splits)
    vectordb = vector_database(chunks)
    retriever = vectordb.as_retriever()
    return retriever

def retriever_qa(file, query):
    retriever_obj = retriever(file)
    qa = RetrievalQA.from_chain_type(llm=llm_model, 
                                chain_type="stuff", 
                                retriever=retriever_obj, 
                                return_source_documents=False)
    response = qa.invoke(query)
    return response['result']
    