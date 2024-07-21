from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Task(BaseModel):
    name: str
    description: Optional[str] = None


@app.get("/")
async def home():
    return {"data": "First Page!"}

@app.get("/tasks")
async def get_tasks():
    task = Task(name="Изучить FastAPI")
    return {"data": task}
