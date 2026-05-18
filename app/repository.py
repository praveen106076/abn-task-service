from datetime import datetime

from app.models import Task
from app.schemas import TaskCreate, TaskUpdate
from app.exceptions import (
    TaskNotFoundException,
    DuplicateTaskException
)


class TaskRepository:

    def __init__(self):
        self.tasks = {}
        self.current_id = 1

    def create(self, task_data: TaskCreate):

        for task in self.tasks.values():
            if task.title.lower() == task_data.title.lower():
                raise DuplicateTaskException(
                    "Task title already exists"
                )

        task = Task(
            id=self.current_id,
            title=task_data.title,
            description=task_data.description,
            status=task_data.status,
            priority=task_data.priority,
            created_at=datetime.utcnow()
        )

        self.tasks[self.current_id] = task

        self.current_id += 1

        return task

    def get_all(
            self,
            status=None,
            sort=None
    ):

        task_list = list(
            self.tasks.values()
        )

        if status:
            task_list = [
                task for task in task_list
                if task.status == status
            ]

        if sort == "priority":
            task_list.sort(
                key=lambda x: x.priority
            )

        return task_list

    def get_by_id(self, task_id: int):

        task = self.tasks.get(
            task_id
        )

        if not task:
            raise TaskNotFoundException(
                "Task not found"
            )

        return task

    def update(
            self,
            task_id: int,
            task_data: TaskUpdate
    ):

        task = self.get_by_id(
            task_id
        )

        update_fields = (
            task_data.model_dump(
                exclude_unset=True
            )
        )

        if "title" in update_fields:

            for existing in self.tasks.values():

                if (
                    existing.id != task_id
                    and existing.title.lower()
                    == update_fields["title"].lower()
                ):
                    raise DuplicateTaskException(
                        "Title already exists"
                    )

        for key, value in update_fields.items():
            setattr(
                task,
                key,
                value
            )

        return task

    def delete(self, task_id):

        if task_id not in self.tasks:
            raise TaskNotFoundException(
                "Task not found"
            )

        del self.tasks[task_id]


repo = TaskRepository()