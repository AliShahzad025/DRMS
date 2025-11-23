# services/volunteer_service.py

from repositories.volunteer_repository import VolunteerRepository
from services.base_service import BaseService
from models.volunteer import Volunteer

class VolunteerService(BaseService):
    def __init__(self, repo: VolunteerRepository):
        super().__init__(repo)

    def list_volunteers(self):
        return self.repo.get_all_volunteers()

    def get_volunteer(self, volunteer_id):
        vol = self.repo.get_volunteer_by_id(volunteer_id)
        if not vol:
            raise ValueError("Volunteer not found")
        return vol

    def create_volunteer(self, payload):
        # Expect payload to include "volunteerID" (existing userID) OR you create user separately.
        if not payload.get("volunteerID"):
            raise ValueError("volunteerID (userID) is required to create a Volunteer record")
        return self.repo.create_volunteer(payload)

    def update_volunteer(self, volunteer_id, payload):
        updated = self.repo.update_volunteer(volunteer_id, payload)
        if updated == 0:
            raise ValueError("Volunteer not found or nothing changed")
        return updated

    def delete_volunteer(self, volunteer_id):
        deleted = self.repo.delete_volunteer(volunteer_id)
        if deleted == 0:
            raise ValueError("Volunteer not found")
        return deleted
