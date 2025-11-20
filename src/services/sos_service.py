# services/sos_service.py
from repositories.sos_repository import SOSRepository
from services.base_service import BaseService

class SOSService(BaseService):
    def __init__(self, repo: SOSRepository):
        super().__init__(repo)

    def list_requests(self):
        return self.repo.get_all_requests()

    def get_request(self, r_id):
        r = self.repo.get_by_id(r_id)
        if not r:
            raise ValueError("SOS Request not found")
        return r

    def create_request(self, payload):
        return self.repo.create_request(payload)

    def update_request(self, r_id, payload):
        updated = self.repo.update_request(r_id, payload)
        if updated == 0:
            raise ValueError("SOS Request not found")
        return updated

    def delete_request(self, r_id):
        deleted = self.repo.delete_by_id("requestID", r_id)
        if deleted == 0:
            raise ValueError("SOS Request not found")
        return deleted

    def compute_priorities(self):
        self.repo.set_priority_scores()
