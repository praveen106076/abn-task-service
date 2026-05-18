from enum import Enum
from datetime import datetime
from pydantic import BaseModel


class TaskStatus(str, Enum):
    NEW = "new"
    IN_PROGRESS = "in progress"
    COMPLETED = "completed"


class Task(BaseModel):
    id: int
    title: str
    description: str | None = None
    status: TaskStatus = TaskStatus.NEW
    priority: int
    created_at: datetime