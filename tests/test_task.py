from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_task():

    response = client.post(
        "/tasks",
        json={
            "title": "Learn FastAPI",
            "description": "Study APIs",
            "priority": 3
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "Learn FastAPI"


def test_duplicate_title():

    response = client.post(
        "/tasks",
        json={
            "title": "Learn FastAPI",
            "priority": 2
        }
    )

    assert response.status_code == 400


def test_get_all_tasks():

    response = client.get(
        "/tasks"
    )

    assert response.status_code == 200


def test_get_single_task():

    response = client.get(
        "/tasks/1"
    )

    assert response.status_code == 200


def test_update_task():

    response = client.put(
        "/tasks/1",
        json={
            "status":
                "completed"
        }
    )

    assert response.status_code == 200


def test_filter_task():

    response = client.get(
        "/tasks?status=completed"
    )

    assert response.status_code == 200


def test_sort_task():

    response = client.get(
        "/tasks?sort=priority"
    )

    assert response.status_code == 200


def test_delete_task():

    response = client.delete(
        "/tasks/1"
    )

    assert response.status_code == 200