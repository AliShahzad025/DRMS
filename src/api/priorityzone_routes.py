from flask import Blueprint, request, jsonify
from db.connection import Database
from repositories.priority_zone_repository import PriorityZoneRepository
from services.priority_zone_service import PriorityZoneService

db = Database()
repo = PriorityZoneRepository(db)
svc = PriorityZoneService(repo)

priorityzone_bp = Blueprint("priorityzone_bp", __name__, url_prefix="/zones")

@priorityzone_bp.route("", methods=["GET"])
def list_zones():
    zs = svc.list_zones()
    return jsonify([z.__dict__ for z in zs]), 200

@priorityzone_bp.route("/<int:zone_id>", methods=["GET"])
def get_zone(zone_id):
    try:
        z = svc.get_zone(zone_id)
        return jsonify(z.__dict__), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@priorityzone_bp.route("", methods=["POST"])
def create_zone():
    payload = request.json or {}
    try:
        new_id = svc.create_zone(payload)
        return jsonify({"zoneID": new_id}), 201
    except Exception as e:
        return jsonify({"error": "failed to create zone", "detail": str(e)}), 500

@priorityzone_bp.route("/<int:zone_id>", methods=["PUT"])
def update_zone(zone_id):
    payload = request.json or {}
    try:
        svc.update_zone(zone_id, payload)
        return jsonify({"status": "updated"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@priorityzone_bp.route("/<int:zone_id>", methods=["DELETE"])
def delete_zone(zone_id):
    try:
        svc.delete_zone(zone_id)
        return jsonify({"status": "deleted"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
