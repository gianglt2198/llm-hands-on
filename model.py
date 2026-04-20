import getpass
import os

from langchain_openrouter import ChatOpenRouter

if not os.getenv("OPENROUTER_API_KEY"):
    os.environ["OPENROUTER_API_KEY"] = getpass.getpass("Enter your OpenRouter API key: ")

def llm_model(params=None):
    model_id = "google/gemma-4-26b-a4b-it"
    default_params = {
        "max_tokens": 256,
        "temperature": 0.5,
        "top_p": 0.2
    }
    if params:
        default_params.update(params)
    llm = ChatOpenRouter(
        model=model_id,        
        **default_params
    )
    return llm