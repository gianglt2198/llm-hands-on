

from models.model import llm
from models.embedding import embeddings

from llama_index.core import (
    Settings 
)

Settings.llm = llm
Settings.embed_model= embeddings
print("✅ LLM and embeddings configured!")