from flask import Blueprint, jsonify, request
from src.models import user_model

user_bp = Blueprint("users", __name__, url_prefix="/users")


@user_bp.route("", methods=["GET"], strict_slashes=False)
@user_bp.route("/", methods=["GET"], strict_slashes=False)
def list_users():
    users = user_model.get_all_users()
    return jsonify(users), 200


@user_bp.route("", methods=["POST"], strict_slashes=False)
@user_bp.route("/", methods=["POST"], strict_slashes=False)
def create_user():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Requisição inválida ou JSON ausente"}), 400

    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return jsonify({"error": "Nome e e-mail são obrigatórios"}), 400

    if user_model.get_user_by_email(email):
        return jsonify({"error": "E-mail já cadastrado"}), 400

    new_user = user_model.create_user(name, email)
    return jsonify(new_user), 201


@user_bp.route("/<int:user_id>", methods=["GET"], strict_slashes=False)
def get_user(user_id):
    user = user_model.get_user_by_id(user_id)
    if not user:
        return jsonify({"error": "Usuário não encontrado"}), 404
    return jsonify(user), 200


@user_bp.route("/<int:user_id>", methods=["PUT"], strict_slashes=False)
def update_user_route(user_id):
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Requisição inválida ou JSON ausente"}), 400

    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return jsonify({"error": "Nome e e-mail são obrigatórios"}), 400

    existing_user = user_model.get_user_by_email(email)
    if existing_user and existing_user["id"] != user_id:
        return jsonify({"error": "E-mail já cadastrado por outro usuário"}), 400

    updated = user_model.update_user(user_id, name, email)
    if not updated:
        return jsonify({"error": "Usuário não encontrado"}), 404

    return jsonify(updated), 200


@user_bp.route("/<int:user_id>", methods=["DELETE"], strict_slashes=False)
def delete_user_route(user_id):
    removed = user_model.delete_user(user_id)
    if not removed:
        return jsonify({"error": "Usuário não encontrado"}), 404
    return jsonify({"message": "Usuário removido com sucesso"}), 200