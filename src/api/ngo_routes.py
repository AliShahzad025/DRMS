# api/ngo_routes.py
from flask import Blueprint, request, jsonify
from db.connection import Database
from repositories.ngo_repository import NGORepository
from services.ngo_service import NGOService

db = Database()
repo = NGORepository(db)
svc = NGOService(repo)
ngo_bp = Blueprint("ngo_bp", __name__, url_prefix="/ngos")

@ngo_bp.route("", methods=["GET"])
def list_ngos():
    ngos = svc.list_ngos()
    return jsonify([ngo.__dict__ for ngo in ngos])

@ngo_bp.route("/<int:ngo_id>", methods=["GET"])
def get_ngo(ngo_id):
    try:
        ngo = svc.get_ngo(ngo_id)
        return jsonify(ngo.__dict__)
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@ngo_bp.route("", methods=["POST"])
def create_ngo():
    payload = request.json
    new_id = svc.create_ngo(payload)
    return jsonify({"ngoID": new_id}), 201

@ngo_bp.route("/<int:ngo_id>", methods=["PUT"])
def update_ngo(ngo_id):
    try:
        svc.update_ngo(ngo_id, request.json)
        return jsonify({"status": "updated"})
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@ngo_bp.route("/<int:ngo_id>", methods=["DELETE"])
def delete_ngo(ngo_id):
    try:
        svc.delete_ngo(ngo_id)
        return jsonify({"status": "deleted"})
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
