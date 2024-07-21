from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Optional, Annotated
from contextlib import asynccontextmanager
from database import create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    print("База данных готова к работе")
    yield
    print("Выключение")


app = FastAPI(lifespan=lifespan)


class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None


class STaskGet(STaskAdd):
    id: int


tasks = []

@app.get("/")
async def home():
    return {"data": "First Page!"}

@app.get("/tasks")
async def get_tasks():
    task = Task(name="Изучить FastAPI")
    return {"data": task}

@app.post("/task")
async def add_task(task: Annotated[STaskAdd, Depends()]):
    tasks.append(task)
    return {"ok": True}

