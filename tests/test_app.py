import pytest
from ACEest_Fitness import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"ACEest Fitness" in response.data


def test_members_page(client):
    response = client.get("/members")

    assert response.status_code == 200
    assert b"Gym Members" in response.data
    assert b"Rahul" in response.data


def test_members_api(client):
    response = client.get("/api/members")

    assert response.status_code == 200

    data = response.get_json()

    assert len(data) == 3
    assert data[0]["name"] == "Rahul"
    assert data[0]["status"] == "Active"


def test_health_endpoint(client):
    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "healthy"
    assert data["application"] == "ACEest Fitness & Gym"
    assert data["version"] == "2.0"


def test_invalid_page(client):
    response = client.get("/invalid-page")

    assert response.status_code == 404
