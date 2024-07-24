

from typing import Annotated
from fastapi import APIRouter, Depends

from repository import TaskRepository
from schemas import STaskAdd


router = APIRouter(
	prefix="/tasks",
	)


@router.post("")
async def add_task(task: Annotated[STaskAdd, Depends()]):
    
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}

@router.get("/profile")
async def get_profile():
    return "todo profile page"

@router.get("")
async def get_tasks():
    tasks = await TaskRepository.get_all()
    return {"tasks": tasks}

