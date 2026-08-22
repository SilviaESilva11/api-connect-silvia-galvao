import pytest
from app import create_app
from src.models.user_model import users_db


@pytest.fixture
def client():
  app = create_app()
  app.config["TESTING"] = True
  with app.test_client() as client:
    with app.app_context():
      users_db.clear()
    yield client


def test_list_users_empty(client):
  response = client.get("/users")
  assert response.status_code == 200
  assert response.get_json() == []


def test_create_user_success(client):
  payload = {"name": "Silvia Galvao", "email": "silvia@email.com"}
  response = client.post("/users", json=payload)
  assert response.status_code == 201
  data = response.get_json()
  assert data["name"] == "Silvia Galvao"
  assert data["email"] == "silvia@email.com"


def test_create_user_missing_fields(client):
  response = client.post("/users", json={"name": "Silvia"})
  assert response.status_code == 400
  assert "error" in response.get_json()


def test_create_user_invalid_json(client):
  response = client.post(
      "/users", data="invalid json", content_type="application/json"
  )
  assert response.status_code == 400


def test_create_user_duplicate_email(client):
  payload = {"name": "Silvia", "email": "silvia@email.com"}
  client.post("/users", json=payload)
  response = client.post("/users", json=payload)
  assert response.status_code == 400
  assert response.get_json()["error"] == "E-mail já cadastrado"


def test_get_user_by_id_success(client):
  res = client.post(
      "/users", json={"name": "Silvia", "email": "silvia@email.com"}
  )
  user_id = res.get_json()["id"]

  response = client.get(f"/users/{user_id}")
  assert response.status_code == 200
  assert response.get_json()["name"] == "Silvia"


def test_get_user_by_id_not_found(client):
  response = client.get("/users/9999")
  assert response.status_code == 404


def test_update_user_success(client):
  res = client.post(
      "/users", json={"name": "Silvia", "email": "silvia@email.com"}
  )
  user_id = res.get_json()["id"]

  payload = {"name": "Silvia Silva", "email": "silvia.novo@email.com"}
  response = client.put(f"/users/{user_id}", json=payload)
  assert response.status_code == 200
  assert response.get_json()["name"] == "Silvia Silva"


def test_update_user_not_found(client):
  payload = {"name": "Nome", "email": "email@email.com"}
  response = client.put("/users/9999", json=payload)
  assert response.status_code == 404


def test_update_user_invalid_json(client):
  res = client.post(
      "/users", json={"name": "Silvia", "email": "silvia@email.com"}
  )
  user_id = res.get_json()["id"]
  response = client.put(
      f"/users/{user_id}",
      data="invalid json",
      content_type="application/json",
  )
  assert response.status_code == 400


def test_update_user_missing_fields(client):
  res = client.post(
      "/users", json={"name": "Silvia", "email": "silvia@email.com"}
  )
  user_id = res.get_json()["id"]
  response = client.put(f"/users/{user_id}", json={"name": "Silvia"})
  assert response.status_code == 400


def test_update_user_duplicate_email(client):
  client.post("/users", json={"name": "User 1", "email": "user1@email.com"})
  res2 = client.post(
      "/users", json={"name": "User 2", "email": "user2@email.com"}
  )
  user2_id = res2.get_json()["id"]

  response = client.put(
      f"/users/{user2_id}",
      json={"name": "User 2 Modificado", "email": "user1@email.com"},
  )
  assert response.status_code == 400


def test_delete_user_success(client):
  res = client.post(
      "/users", json={"name": "Silvia", "email": "silvia@email.com"}
  )
  user_id = res.get_json()["id"]

  response = client.delete(f"/users/{user_id}")
  assert response.status_code == 200
  assert response.get_json()["message"] == "Usuário removido com sucesso"


def test_delete_user_not_found(client):
  response = client.delete("/users/9999")
  assert response.status_code == 404


def test_update_user_model_not_found():
  from src.models.user_model import update_user

  result = update_user(9999, "Nome", "email@email.com")
  assert result is None