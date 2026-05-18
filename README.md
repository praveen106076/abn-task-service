# Task Service

Simple task service built using FastAPI

## Features

- Create task
- Update task
- Delete task
- Get all tasks
- Get task by id
- Filter by status
- Sort by priority
- In-memory repository
- Exception handling
- Unit tests

## Project Structure

```text
app/
    main.py
    models.py
    schemas.py
    repository.py
    exceptions.py
    routes.py

tests/
    test_task.py
```

Install:

```bash
pip install -r requirements.txt
```

Run application:

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

Run tests:

```bash
pytest
```