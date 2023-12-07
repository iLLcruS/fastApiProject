from typing import List

from fastapi import APIRouter, HTTPException

from .crud import get_tasks, get_task, create_task, update_task, delete_task
from .models import Task

router = APIRouter()


@router.get("/tasks/", response_model=List[Task])
def read_tasks(skip: int = 0, limit: int = 10):
    return get_task(skip=skip, limit=limit)


@router.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: int):
    task = get_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Http Error 404 [Task not found]")
    return task
