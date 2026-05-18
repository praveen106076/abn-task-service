# Task Service

A lightweight task service built with FastAPI using an in-memory repository.  
The application provides CRUD operations for tasks along with filtering, sorting, exception handling, and tests.

## Approach

The application was designed with separation of concerns in mind:

- `models.py` → Defines task entity and status enum
- `schemas.py` → Request/response validation models
- `repository.py` → In-memory data storage and CRUD logic
- `routes.py` → FastAPI endpoints
- `exceptions.py` → Custom exception handling
- `tests/` → API tests using pytest and FastAPI TestClient
---

## Assumptions

- Task titles must be unique
- Priority values are restricted from 1–5
- Data is stored in memory and will reset after application restart
- Task IDs are auto-generated and incremented sequentially
- Tasks are created with default status `new` if no status is supplied

---

## Features

- Create task
- List all tasks
- Get task by ID
- Update task
- Delete task
- Filter by task status
- Sort by priority
- Custom exception handling
- In-memory repository
- Unit tests

---

## Project Structure

```text
task-service/

app/
    main.py
    models.py
    schemas.py
    repository.py
    exceptions.py
    routes.py

tests/
    test_task.py

requirements.txt
README.md
```

---

## Installation

Create virtual environment:

```bash
python -m venv .venv
```

Activate environment:

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
uvicorn app.main:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

## Run Tests

```bash
python -m pytest
```

---

## API Examples

Create Task:

POST `/tasks`

```json
{
    "title":"Hi Praveen",
    "description":"Praveen Tasks service",
    "priority":3
}
```

Filter by status:

```text
GET /tasks?status=completed
```

Sort by priority:

```text
GET /tasks?sort=priority
```