import getpass
import os

if not os.getenv("OPENROUTER_API_KEY"):
    os.environ["OPENROUTER_API_KEY"] = getpass.getpass("Enter your OpenRouter API key: ")

MODEL_ID = "google/gemma-4-26b-a4b-it"
DEFAULT_PARAMS = {
    "max_tokens": 256,
    "temperature": 0.5,
    "top_p": 0.2,
}

