from fastapi import APIRouter
from agents.langgraph_agent import run_agent

router = APIRouter()

@router.post("/ask")
def ask_ai(question: str):
    answer = run_agent(question)

    return {
        "question": question,
        "response": answer
    }