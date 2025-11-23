# ==============================================
# API: api/resource_routes.py
# ==============================================
from flask import Blueprint, jsonify, request
from db.connection import Database
from repositories.resource_repository import ResourceRepository
from services.resource_service import ResourceService

db = Database()
repo = ResourceRepository(db)
service = ResourceService(repo)

resource_bp = Blueprint("resource_bp", __name__, url_prefix="/resources")

# -----------------------------
# ResourceType CRUD Endpoints
# -----------------------------
@resource_bp.route("/types", methods=["GET"])
def get_resource_types():
    types = service.get_all_types()
    return jsonify([t.__dict__ for t in types]), 200

@resource_bp.route("/types/<int:type_id>", methods=["GET"])
def get_resource_type(type_id):
    try:
        t = service.get_type(type_id)
        return jsonify(t.__dict__), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@resource_bp.route("/types", methods=["POST"])
def create_resource_type():
    payload = request.json or {}
    try:
        new_id = service.create_type(payload)
        return jsonify({"resourceTypeID": new_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@resource_bp.route("/types/<int:type_id>", methods=["PUT"])
def update_resource_type(type_id):
    payload = request.json or {}
    try:
        service.update_type(type_id, payload)
        return jsonify({"status": "updated"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@resource_bp.route("/types/<int:type_id>", methods=["DELETE"])
def delete_resource_type(type_id):
    try:
        service.delete_type(type_id)
        return jsonify({"status": "deleted"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

# -----------------------------
# ResourceStock CRUD Endpoints
# -----------------------------
@resource_bp.route("", methods=["GET"])
def get_resources():
    resources = service.get_all_resources()
    return jsonify([r.__dict__ for r in resources]), 200

@resource_bp.route("/<int:resource_id>", methods=["GET"])
def get_resource(resource_id):
    try:
        r = service.get_resource(resource_id)
        return jsonify(r.__dict__), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@resource_bp.route("", methods=["POST"])
def create_resource():
    payload = request.json or {}
    try:
        new_id = service.create_resource(payload)
        return jsonify({"resourceID": new_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@resource_bp.route("/<int:resource_id>", methods=["PUT"])
def update_resource(resource_id):
    payload = request.json or {}
    try:
        service.update_resource(resource_id, payload)
        return jsonify({"status": "updated"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@resource_bp.route("/<int:resource_id>", methods=["DELETE"])
def delete_resource(resource_id):
    try:
        service.delete_resource(resource_id)
        return jsonify({"status": "deleted"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

# -----------------------------
# Specialized Actions
# -----------------------------
@resource_bp.route("/<int:resource_id>/add", methods=["POST"])
def add_resource(resource_id):
    payload = request.json or {}
    try:
        service.add_stock(resource_id, payload)
        return jsonify({"status": "stock added"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@resource_bp.route("/<int:resource_id>/update", methods=["POST"])
def update_resource_stock(resource_id):
    payload = request.json or {}
    try:
        service.update_stock(resource_id, payload)
        return jsonify({"status": "stock updated"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@resource_bp.route("/<int:resource_id>/transfer", methods=["POST"])
def transfer_resource(resource_id):
    payload = request.json or {}
    try:
        service.transfer_resource(resource_id, payload)
        return jsonify({"status": "transfer initiated"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@resource_bp.route("/<int:resource_id>/allocate", methods=["POST"])
def allocate_resource(resource_id):
    payload = request.json or {}
    try:
        service.allocate_resource(resource_id, payload)
        return jsonify({"status": "resource allocated"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400