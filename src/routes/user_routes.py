from flask import Blueprint, jsonify, request
from src.models.user_model import (
    create_user,
    get_all_users,
    get_user_by_id,
)

user_router = Blueprint("user_router", __name__)


# 1. Leitura Geral (HTTP 200)
@user_router.route("/", methods=["GET"])
def list_users():
    users = get_all_users()
    return (
        jsonify(
            {
                "status": "success",
                "total": len(users),
                "data": [u.to_dict() for u in users],
            }
        ),
        200,
    )


# 2. Busca de ID Inexistente (HTTP 404)
@user_router.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = get_user_by_id(user_id)
    if not user:
        return jsonify({"status": "error", "message": "Usuario nao encontrado."}), 404
    return jsonify({"status": "success", "data": user.to_dict()}), 200


# 3. Criação Padrão via POST (HTTP 201 ou 400)
@user_router.route("/", methods=["POST"])
def add_user():
    data = request.get_json() or {}
    name = data.get("name")
    email = data.get("email")

    if not email:
        return (
            jsonify(
                {"status": "error", "message": "O campo email e obrigatorio."}
            ),
            400,
        )

    user = create_user(name, email)
    return (
        jsonify(
            {
                "status": "success",
                "message": "Usuario criado com sucesso.",
                "data": user.to_dict(),
            }
        ),
        201,
    )


# 4. Rota para teste via Navegador no GET (HTTP 201 ou 400)
@user_router.route("/create", methods=["GET"])
def add_user_via_url():
    name = request.args.get("name", "Usuario Teste")
    email = request.args.get("email", "")

    if not email:
        return (
            jsonify(
                {"status": "error", "message": "O campo email e obrigatorio."}
            ),
            400,
        )

    user = create_user(name, email)
    return (
        jsonify(
            {
                "status": "success",
                "message": "Usuario criado com sucesso.",
                "data": user.to_dict(),
            }
        ),
        201,
    )