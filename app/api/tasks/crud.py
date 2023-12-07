from typing import List, Optional

from .models import Task

tasks = []


def get_tasks(skip: int = 0, limit: int = 10) -> List[Task]:
    return tasks[skip: skip + limit]


def get_task(task_id: int) -> Optional[Task]:
    for task in tasks:
        if task.id == task_id:
            return task
        return None


def create_task(task: Task) -> Task:
    tasks.append(task)
    return task


def delete_task(task_id: int) -> Optional[Task]:
    for i, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(i)
            return delete_task
    return None


def update_task(task_id: int, updated_task: Task) -> Optional[Task]:
    for i, task in enumerate(tasks):
        if task.id == task_id:
            tasks[i] = updated_task
            return updated_task
    return None
