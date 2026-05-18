from fastapi import (
    APIRouter,
    HTTPException,
    Query
)

from app.repository import repo
from app.schemas import (
    TaskCreate,
    TaskUpdate
)

from app.exceptions import (
    TaskNotFoundException,
    DuplicateTaskException
)

router = APIRouter()


@router.post("/tasks")
def create_task(data: TaskCreate):

    try:
        return repo.create(data)

    except DuplicateTaskException as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get("/tasks")
def get_tasks(
        status: str = Query(
            None
        ),
        sort: str = Query(
            None
        )
):

    return repo.get_all(
        status,
        sort
    )


@router.get("/tasks/{task_id}")
def get_task(task_id: int):

    try:
        return repo.get_by_id(
            task_id
        )

    except TaskNotFoundException as e:

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


@router.put("/tasks/{task_id}")
def update_task(
        task_id: int,
        data: TaskUpdate
):

    try:
        return repo.update(
            task_id,
            data
        )

    except (
            TaskNotFoundException,
            DuplicateTaskException
    ) as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):

    try:

        repo.delete(
            task_id
        )

        return {
            "message":
                "Task deleted successfully"
        }

    except TaskNotFoundException as e:

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )