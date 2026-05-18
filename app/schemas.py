from pydantic import BaseModel, Field
from app.models import TaskStatus


class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    status: TaskStatus = TaskStatus.NEW
    priority: int = Field(ge=1, le=5)


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: TaskStatus | None = None
    priority: int | None = Field(None, ge=1, le=5)