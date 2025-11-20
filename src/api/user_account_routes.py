# api/user_account_routes.py

from flask import Blueprint, jsonify, request
from db.connection import Database
from repositories.user_account_repository import UserAccountRepository
from services.user_account_service import UserAccountService

db = Database()
repo = UserAccountRepository(db)
service = UserAccountService(repo)

user_bp= Blueprint("user_bp", __name__, url_prefix="/users")

@user_bp.route("", methods=["GET"])
def list_users():
    users = service.list_users()
    return jsonify([u.to_dict() for u in users]), 200

@user_bp.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    try:
        user = service.get_user(user_id)
        return jsonify(user.to_dict())
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@user_bp.route("", methods=["POST"])
def create_user():
    payload = request.get_json(force=True)
    try:
        user = service.create_user(payload)
        return jsonify(user.to_dict()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@user_bp.route("/<int:user_id>", methods=["PUT", "PATCH"])
def update_user(user_id):
    payload = request.get_json(force=True)
    try:
        user = service.update_user(user_id, payload)
        return jsonify(user.to_dict()), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@user_bp.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    try:
        service.delete_user(user_id)
        return jsonify({"status": "deleted"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

# ----- LOGIN -----
@user_bp.route("/login", methods=["POST"])
def login():
    payload = request.get_json(force=True)
    try:
        user = service.login(payload["email"], payload["password"])
        return jsonify(user.to_dict()), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 401
