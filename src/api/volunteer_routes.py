# api/volunteer_routes.py

from flask import Blueprint, request, jsonify
from db.connection import Database
from repositories.volunteer_repository import VolunteerRepository
from services.volunteer_service import VolunteerService

db = Database()
repo = VolunteerRepository(db)
svc = VolunteerService(repo)

volunteer_bp = Blueprint("volunteer_bp", __name__, url_prefix="/volunteers")

@volunteer_bp.route("", methods=["GET"])
def list_volunteers():
    volunteers = svc.list_volunteers()
    # convert to dicts
    return jsonify([v.__dict__ for v in volunteers]), 200

@volunteer_bp.route("/<int:volunteer_id>", methods=["GET"])
def get_volunteer(volunteer_id):
    try:
        volunteer = svc.get_volunteer(volunteer_id)
        return jsonify(volunteer.__dict__), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@volunteer_bp.route("", methods=["POST"])
def create_volunteer():
    payload = request.json or {}
    try:
        new_id = svc.create_volunteer(payload)
        return jsonify({"volunteerID": new_id}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "failed to create volunteer", "detail": str(e)}), 500

@volunteer_bp.route("/<int:volunteer_id>", methods=["PUT"])
def update_volunteer(volunteer_id):
    payload = request.json or {}
    try:
        svc.update_volunteer(volunteer_id, payload)
        return jsonify({"status": "updated"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": "failed to update volunteer", "detail": str(e)}), 500

@volunteer_bp.route("/<int:volunteer_id>", methods=["DELETE"])
def delete_volunteer(volunteer_id):
    try:
        svc.delete_volunteer(volunteer_id)
        return jsonify({"status": "deleted"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": "failed to delete volunteer", "detail": str(e)}), 500
