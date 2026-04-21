from langchain_openrouter import ChatOpenRouter
from langchain_openai import OpenAIEmbeddings

from config import MODEL_COMPLETION, DEFAULT_PARAMS, MODEL_EMBEDDING, OPENROUTER_API_BASE, OPENROUTER_API_KEY

llm_model = ChatOpenRouter(
    model=MODEL_COMPLETION,
    **DEFAULT_PARAMS
)

embedding_model = OpenAIEmbeddings(
    model=MODEL_EMBEDDING,
    openai_api_base=OPENROUTER_API_BASE,
    openai_api_key=OPENROUTER_API_KEY,
    check_embedding_ctx_length= False,
    encoding_format="float"
)

def generate_response(query):
    return llm_model.invoke(query).content