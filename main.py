from fastapi import FastAPI, Request, Depends, HTTPException
from contextlib import asynccontextmanager
from router import router as tasks_router
from database import create_tables
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordBearer, HTTPBasic, HTTPBasicCredentials
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

secret_user : str = "User"
secret_password: str = "secret"

basic: HTTPBasicCredentials = HTTPBasic()



@app.get("/", response_class=HTMLResponse)
async def home(request:Request):
    """Стартовая страница"""
    return templates.TemplateResponse(request=request, name="index.html")

@app.get("/about_me/", response_class=HTMLResponse)
async def get_about_me(request: Request):
    return templates.TemplateResponse(request=request, name="about_me.html")

@app.get("/who")
async def get_who(
    creds: HTTPBasicCredentials = Depends(basic)) -> dict:
    if(creds.username == secret_user and creds.password == secret_password):
        return {"username": creds.username, "password": creds.password, "WOW": "You cool a hacker!!!"}
    raise HTTPException(status_code=401, detail="Hey!")

@app.get("/login")
async def login(creds: HTTPBasicCredentials = Depends(basic)) -> dict:
    rules_admin = """Beautiful is better than ugly.
                        Explicit is better than implicit.
                        Simple is better than complex.
                        Complex is better than complicated.
                        Flat is better than nested.
                        Sparse is better than dense.
                        Readability counts.
                        Special cases aren't special enough to break the rules.
                        Although practicality beats purity.
                        Errors should never pass silently.
                        Unless explicitly silenced.
                        In the face of ambiguity, refuse the temptation to guess.
                        There should be one-- and preferably only one --obvious way to do it.
                        Although that way may not be obvious at first unless you're Dutch.
                        Now is better than never.
                        Although never is often better than *right* now.
                        If the implementation is hard to explain, it's a bad idea.
                        If the implementation is easy to explain, it may be a good idea. """
    if(creds.username == "Admin" and creds.password == "secret"):
        return {"data": "Hi Admin on API", "msg": rules_admin}
    raise HTTPException(status_code=401, detail="Sorry you're not admin on site!!!")

@app.get("/secret", response_class=HTMLResponse)
async def get_secret_page(request: Request):
    return templates.TemplateResponse(request=request, name="secret.html")