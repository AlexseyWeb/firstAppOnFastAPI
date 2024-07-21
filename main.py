from fastapi import FastAPI
from contextlib import asynccontextmanager
from router import router as tasks_router
from database import create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    print("База данных готова к работе")
    yield
    print("Выключение")


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)


@app.get("/")
async def home():
    return {"data": "First Page!"}


