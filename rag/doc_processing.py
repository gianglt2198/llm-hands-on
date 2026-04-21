import wget

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_chroma import Chroma

from embedding import embeddings

FILENAME = 'companyPolicies.txt'
URL = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/6JDbUb_L3egv_eOkouY71A.txt'

# wget.download(URL, out=FILENAME)
# print(f"Downloaded {FILENAME}")

loader = TextLoader(FILENAME)
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

docsearch = Chroma.from_documents(documents=texts, embedding=embeddings)
print('document ingested')