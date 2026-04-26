import os
import getpass

if not os.getenv("OPENROUTER_API_KEY"):
    os.environ["OPENROUTER_API_KEY"] = getpass.getpass("Enter your OpenRouter API key: ")

OPENROUTER_API_BASE = "https://openrouter.ai/api/v1"
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

MODEL_EMBEDDING = "nvidia/llama-nemotron-embed-vl-1b-v2:free"
MODEL_COMPLETION = "google/gemma-4-26b-a4b-it"

DEFAULT_PARAMS = {
    "max_tokens": 256,
    "temperature": 0.5,
    "top_p": 0.2,
}
