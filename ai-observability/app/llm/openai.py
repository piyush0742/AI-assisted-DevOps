from openai import OpenAI
from app.llm.base import LLMClient
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class OpenAIClient(LLMClient):
    def summarize(self, text: str) -> str:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a DevOps log analysis expert"},
                {"role": "user", "content": f"Summarize these logs:\n{text}"}
            ]
        )
        return response.choices[0].message.content

    def explain_error(self, text: str) -> str:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": f"Explain root cause of this error:\n{text}"}
            ]
        )
        return response.choices[0].message.content
