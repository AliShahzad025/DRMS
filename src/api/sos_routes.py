# api/sos_routes.py
from flask import Blueprint, request, jsonify
from db.connection import Database
from repositories.sos_repository import SOSRepository
from services.sos_service import SOSService

db = Database()
repo = SOSRepository(db)
svc = SOSService(repo)
sos_bp = Blueprint("sos_bp", __name__, url_prefix="/sos")

@sos_bp.route("", methods=["GET"])
def list_sos():
    items = svc.list_requests()
    return jsonify([i.__dict__ for i in items])

@sos_bp.route("/<int:rid>", methods=["GET"])
def get_sos(rid):
    try:
        r = svc.get_request(rid)
        return jsonify(r.__dict__)
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@sos_bp.route("", methods=["POST"])
def create_sos():
    payload = request.json
    new_id = svc.create_request(payload)
    return jsonify({"requestID": new_id}), 201

@sos_bp.route("/<int:rid>", methods=["PUT"])
def update_sos(rid):
    try:
        svc.update_request(rid, request.json)
        return jsonify({"status": "updated"})
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@sos_bp.route("/<int:rid>", methods=["DELETE"])
def delete_sos(rid):
    try:
        svc.delete_request(rid)
        return jsonify({"status": "deleted"})
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@sos_bp.route("/recompute-priorities", methods=["POST"])
def recompute_priorities():
    svc.compute_priorities()
    return jsonify({"status": "priorities recomputed"})
