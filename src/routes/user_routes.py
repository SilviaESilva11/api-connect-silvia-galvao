# src/routes/user_routes.py

from flask import Blueprint, jsonify, request
from src.models.user_model import (
    create_user,
    delete_user,
    get_all_users,
    get_user_by_email,
    get_user_by_id,
    update_user,
)

user_bp = Blueprint("users", __name__, url_prefix="/users")


@user_bp.route("/", methods=["GET"])
def list_users():
    return jsonify(get_all_users()), 200


@user_bp.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = get_user_by_id(user_id)
    if not user:
        return jsonify({"error": "Usuário não encontrado"}), 404
    return jsonify(user), 200


@user_bp.route("/", methods=["POST"])
def register_user():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Requisição deve ser um JSON válido"}), 400

    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return jsonify({"error": "Nome e e-mail são obrigatórios"}), 400

    if get_user_by_email(email):
        return jsonify({"error": "E-mail já cadastrado"}), 400

    user = create_user(name, email)
    return jsonify(user), 201


@user_bp.route("/<int:user_id>", methods=["PUT"])
def edit_user(user_id):
    user = get_user_by_id(user_id)
    if not user:
        return jsonify({"error": "Usuário não encontrado"}), 404

    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Requisição deve ser um JSON válido"}), 400

    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return jsonify({"error": "Nome e e-mail são obrigatórios"}), 400

    # Verifica se o e-mail pertence a OUTRO usuário
    existing_user = get_user_by_email(email)
    if existing_user and existing_user["id"] != user_id:
        return jsonify({"error": "E-mail já está em uso por outro usuário"}), 400

    updated = update_user(user_id, name, email)
    return jsonify(updated), 200


@user_bp.route("/<int:user_id>", methods=["DELETE"])
def remove_user(user_id):
    if not delete_user(user_id):
        return jsonify({"error": "Usuário não encontrado"}), 404
    return jsonify({"message": "Usuário removido com sucesso"}), 200