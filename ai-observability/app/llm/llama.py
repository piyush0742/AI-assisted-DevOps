import requests
from app.llm.base import BaseLLM

class LlamaClient(BaseLLM):

    def summarize(self, text: str) -> str:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": f"Summarize this Kubernetes log:\n{text}",
                "stream": False
            }
        )
        return response.json()["response"]

    def explain_error(self, text: str) -> str:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": (
                    "You are a Kubernetes SRE.\n"
                    "Explain the root cause and fix for this error:\n"
                    f"{text}"
                ),
                "stream": False
            }
        )
        return response.json()["response"]
