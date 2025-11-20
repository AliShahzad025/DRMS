from flask import Blueprint, jsonify
from db.connection import Database
from repositories.admin_repository import AdminRepository
from services.admin_service import AdminService

db = Database()
admin_repo = AdminRepository(db)
admin_service = AdminService(admin_repo)

admin_bp = Blueprint("admin_bp", __name__)

@admin_bp.route("/admins", methods=["GET"])
def get_all_admins():
    admins = admin_service.list_admins()
    return jsonify([admin.__dict__ for admin in admins])

@admin_bp.route("/admins/<int:admin_id>", methods=["GET"])
def get_admin(admin_id):
    try:
        admin = admin_service.get_admin(admin_id)
        return jsonify(admin.__dict__)
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
