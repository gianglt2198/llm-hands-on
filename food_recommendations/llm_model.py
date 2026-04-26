from langchain_openrouter import ChatOpenRouter

from config import MODEL_COMPLETION, DEFAULT_PARAMS

llm = ChatOpenRouter(
    model=MODEL_COMPLETION,
    **DEFAULT_PARAMS
)