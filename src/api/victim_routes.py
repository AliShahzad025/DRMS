from flask import Blueprint, request, jsonify
from db.connection import Database
from repositories.victim_repository import VictimRepository
from services.victim_service import VictimService

db = Database()
repo = VictimRepository(db)
svc = VictimService(repo)

victim_bp = Blueprint("victim_bp", __name__, url_prefix="/victims")

@victim_bp.route("", methods=["GET"])
def list_victims():
    vs = svc.list_victims()
    return jsonify([v.__dict__ for v in vs]), 200

@victim_bp.route("/<int:victim_id>", methods=["GET"])
def get_victim(victim_id):
    try:
        v = svc.get_victim(victim_id)
        return jsonify(v.__dict__), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@victim_bp.route("", methods=["POST"])
def create_victim():
    payload = request.json or {}
    try:
        new = svc.create_victim(payload)
        return jsonify({"victimID": new}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "failed to create victim", "detail": str(e)}), 500

@victim_bp.route("/<int:victim_id>", methods=["PUT"])
def update_victim(victim_id):
    payload = request.json or {}
    try:
        svc.update_victim(victim_id, payload)
        return jsonify({"status": "updated"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@victim_bp.route("/<int:victim_id>", methods=["DELETE"])
def delete_victim(victim_id):
    try:
        svc.delete_victim(victim_id)
        return jsonify({"status": "deleted"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
