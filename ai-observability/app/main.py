from fastapi import FastAPI
from app.services.summarizer import get_llm

app = FastAPI(title="AI Observability Service")

@app.post("/summarize")
def summarize(payload: dict):
    llm = get_llm()
    return {
        "summary": llm.summarize(payload["logs"])
    }

@app.post("/explain")
def explain(payload: dict):
    llm = get_llm()
    return {
        "analysis": llm.explain_error(payload["logs"])
    }
