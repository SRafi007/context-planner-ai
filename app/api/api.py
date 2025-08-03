from fastapi import FastAPI, Body
from app.context.context import ctx, init_llm
from app.llm.llm_engine import generate_reply
from app.core.executor import execute_intent
from app.core.query import search_tasks
from app.llm.summarizer import generate_summary

app = FastAPI()
init_llm("mistral")


@app.post("/reply")
def reply(input: str = Body(..., embed=True)):
    response = generate_reply(ctx.context, input)
    return {"response": response, "context": ctx.context}


@app.post("/execute")
def execute():
    result = execute_intent(ctx.context)
    return {"result": result}


@app.get("/summary")
def summary():
    return {"summary": generate_summary()}


@app.get("/search")
def search(query: str):
    return {"results": search_tasks(query)}
