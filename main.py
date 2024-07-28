from fastapi import FastAPI, Request, Depends
from contextlib import asynccontextmanager
from router import router as tasks_router
from database import create_tables
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    print("База данных готова к работе")
    yield
    print("Выключение")


app = FastAPI(lifespan=lifespan, title="Задачи")
app.include_router(tasks_router)
templates = Jinja2Templates(directory="templates")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/", response_class=HTMLResponse)
async def home(request:Request):
    """Стартовая страница"""
    return templates.TemplateResponse(request=request, name="index.html")

@app.get("/about_me/", response_class=HTMLResponse)
async def get_about_me(request: Request):
    return templates.TemplateResponse(request=request, name="about_me.html")

@app.get("/login")
async def login(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token" : token}

