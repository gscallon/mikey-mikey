import pytest
from pytest_mock import MockFixture
from app import app # Flask instance of the API


@pytest.fixture
def client():
    app.config.update({"TESTING": True})

    with app.test_client() as client:
        yield client

def test_elapsed(client):
    response = client.get("/")
    assert response.status_code == 200
    # assert b"Welcome to the home page" in response.data

def test_route(client):
    response = client.get("/")
    assert response.status_code == 200
    # assert b"I am a software engineer" in response.data