import requests
from app.llm.base import LLMClient

class LlamaClient(LLMClient):
    def summarize(self, text: str) -> str:
        r = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": f"Summarize these logs:\n{text}",
                "stream": False
            }
        )
        return r.json()["response"]

    def explain_error(self, text: str) -> str:
        r = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": f"Explain the root cause of this error:\n{text}",
                "stream": False
            }
        )
        return r.json()["response"]
