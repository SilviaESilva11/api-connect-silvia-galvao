import pytest
from app import create_app
from src.models.user_model import db


@pytest.fixture
def client():
    app = create_app("sqlite:///:memory:")
    app.config["TESTING"] = True

    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()
        db.engine.dispose()


# 1. Criação com sucesso (201 Created)
def test_create_user_success(client):
    payload = {"name": "Silvia Galvao", "email": "silvia@email.com"}
    response = client.post("/users/", json=payload)
    data = response.get_json()

    assert response.status_code == 201
    assert data["status"] == "success"
    assert data["data"]["name"] == "Silvia Galvao"


# 2. Falha na criação / Validação (400 Bad Request)
def test_create_user_missing_email_failure(client):
    payload = {"name": "Silvia Galvao"}  # Sem e-mail
    response = client.post("/users/", json=payload)
    data = response.get_json()

    assert response.status_code == 400
    assert data["status"] == "error"


# 3. Listagem geral (200 OK)
def test_list_users_success(client):
    client.post(
        "/users/", json={"name": "Silvia Galvao", "email": "silvia@email.com"}
    )
    response = client.get("/users/")
    data = response.get_json()

    assert response.status_code == 200
    assert data["status"] == "success"


# 4. Falha na busca (404 Not Found)
def test_get_user_not_found_failure(client):
    response = client.get("/users/9999")
    data = response.get_json()

    assert response.status_code == 404
    assert data["status"] == "error"