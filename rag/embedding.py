from langchain_openai import OpenAIEmbeddings

from config import MODEL_EMBEDDING, OPENROUTER_API_BASE, OPENROUTER_API_KEY

embeddings = OpenAIEmbeddings(
    model=MODEL_EMBEDDING,
    openai_api_base=OPENROUTER_API_BASE,
    openai_api_key=OPENROUTER_API_KEY,
    check_embedding_ctx_length= False,
    encoding_format="float"
)