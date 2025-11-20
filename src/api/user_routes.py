from flask import Blueprint, jsonify, request
from services.user_services import UserService
from repositories.user_repository import UserRepository
from db.connection import Database

# Setup dependencies (temporary for now)
db = Database()
user_repo = UserRepository(db)
user_service = UserService(user_repo)

# Create Blueprint
user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/users", methods=["GET"])
def get_all_users():
    users = user_service.get_all_users()
    return jsonify([user.__dict__ for user in users])

@user_bp.route("/users/<int:user_id>", methods=["GET"])
def get_user_by_id(user_id):
    try:
        user = user_service.get_user_by_id(user_id)
        return jsonify(user.__dict__)
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@user_bp.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    try:
        new_user = user_service.create_user(data)
        return jsonify(new_user.__dict__), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@user_bp.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    try:
        user_service.delete_user(user_id)
        return jsonify({"message": f"User {user_id} deleted successfully"})
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
