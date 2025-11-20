# services/ngo_service.py
from repositories.ngo_repository import NGORepository
from services.base_service import BaseService

class NGOService(BaseService):
    def __init__(self, repo: NGORepository):
        super().__init__(repo)

    def list_ngos(self):
        return self.repo.get_all_ngos()

    def get_ngo(self, ngo_id):
        ngo = self.repo.get_ngo_by_id(ngo_id)
        if not ngo:
            raise ValueError("NGO not found")
        return ngo

    def create_ngo(self, payload):
        return self.repo.create_ngo(payload)

    def update_ngo(self, ngo_id, payload):
        updated = self.repo.update_ngo(ngo_id, payload)
        if updated == 0:
            raise ValueError("NGO not found or nothing changed")
        return updated

    def delete_ngo(self, ngo_id):
        deleted = self.repo.delete_by_id("ngoID", ngo_id)
        if deleted == 0:
            raise ValueError("NGO not found")
        return deleted
