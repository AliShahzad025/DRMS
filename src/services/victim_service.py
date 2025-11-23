from repositories.victim_repository import VictimRepository
from services.base_service import BaseService
from models.victim import Victim

class VictimService(BaseService):
    def __init__(self, repo: VictimRepository):
        super().__init__(repo)

    def list_victims(self):
        return self.repo.get_all_victims()

    def get_victim(self, victim_id):
        v = self.repo.get_victim_by_id(victim_id)
        if not v:
            raise ValueError("Victim not found")
        return v

    def create_victim(self, payload):
        if not payload.get("victimID"):
            raise ValueError("victimID (userID) required")
        return self.repo.create_victim(payload)

    def update_victim(self, victim_id, payload):
        rc = self.repo.update_victim(victim_id, payload)
        if rc == 0:
            raise ValueError("Victim not found or nothing changed")
        return rc

    def delete_victim(self, victim_id):
        rc = self.repo.delete_victim(victim_id)
        if rc == 0:
            raise ValueError("Victim not found")
        return rc
