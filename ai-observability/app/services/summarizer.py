from app.llm.llama import LlamaClient
import os

def get_llm():
    provider = os.getenv("LLM_PROVIDER", "llama")

    if provider == "llama":
        return LlamaClient()

    raise ValueError(f"Unsupported LLM provider: {provider}")

