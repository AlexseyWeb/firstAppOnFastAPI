from typing import Annotated
from fastapi import APIRouter, Depends
from repository import TaskRepository, UsersRepository
from schemas import STaskAdd, SUser


router = APIRouter(
	prefix="/tasks",
	)



@router.post("")
async def add_task(task: Annotated[STaskAdd, Depends()]):
    """Добавить задачу в базу данных"""
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}

@router.get("/profile")
async def get_profile():
    """Получить профайл пользователя"""
    return "todo profile page"

@router.get("")
async def get_tasks():
    """Получить все задание из базы данных"""
    tasks = await TaskRepository.get_all()
    return {"tasks": tasks}


@router.post("/user")
async def add_user(user: Annotated[SUser, Depends()]):
    """Добавить пользователя в базу данных"""
    user_id = await UsersRepository.add_one(user)
    return {"ok": True, "user_id": user_id}

@router.get("/user")
async def get_user():
    users = await UsersRepository.get_all()
    return {"users": users}




