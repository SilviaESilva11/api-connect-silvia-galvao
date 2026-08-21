import pytest
from app import create_app
from src.models.user_model import db


@pytest.fixture
def client():
    """Cria uma instancia de teste do aplicativo Flask com banco em memoria."""
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()


def test_list_users(client):
    """Testa a listagem geral de usuarios (200 OK)."""
    response = client.get("/users/")
    assert response.status_code == 200
    assert response.json["status"] == "success"


def test_create_user_success(client):
    """Testa a criacao de usuario via POST (201 Created)."""
    payload = {"name": "Silvia", "email": "silvia@email.com"}
    response = client.post("/users/", json=payload)
    assert response.status_code == 201
    assert response.json["status"] == "success"


def test_get_user_by_id_success(client):
    """Testa a busca de usuario existente por ID (200 OK)."""
    create_resp = client.post(
        "/users/", json={"name": "Ana", "email": "ana@email.com"}
    )
    user_id = create_resp.json["data"]["id"]

    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json["data"]["name"] == "Ana"


def test_get_user_not_found(client):
    """Testa a busca por ID inexistente (404 Not Found)."""
    response = client.get("/users/999")
    assert response.status_code == 404
    assert response.json["status"] == "error"


def test_create_user_missing_email(client):
    """Testa a criacao sem email via POST (400 Bad Request)."""
    response = client.post("/users/", json={"name": "Sem Email"})
    assert response.status_code == 400
    assert response.json["status"] == "error"


def test_create_user_via_url_success(client):
    """Testa a rota GET /create com parametros validos (201 Created)."""
    response = client.get("/users/create?name=Carlos&email=carlos@email.com")
    assert response.status_code == 201
    assert response.json["status"] == "success"


def test_create_user_via_url_missing_email(client):
    """Testa a rota GET /create sem email na URL (400 Bad Request)."""
    response = client.get("/users/create?name=Carlos")
    assert response.status_code == 400
    assert response.json["status"] == "error"