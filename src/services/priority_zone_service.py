from repositories.priority_zone_repository import PriorityZoneRepository
from services.base_service import BaseService

class PriorityZoneService(BaseService):
    def __init__(self, repo: PriorityZoneRepository):
        super().__init__(repo)

    def list_zones(self):
        return self.repo.get_all_zones()

    def get_zone(self, zone_id):
        z = self.repo.get_zone(zone_id)
        if not z:
            raise ValueError("Zone not found")
        return z

    def create_zone(self, payload):
        return self.repo.create_zone(payload)

    def update_zone(self, zone_id, payload):
        rc = self.repo.update_zone(zone_id, payload)
        if rc == 0:
            raise ValueError("Zone not found or nothing changed")
        return rc

    def delete_zone(self, zone_id):
        rc = self.repo.delete_zone(zone_id)
        if rc == 0:
            raise ValueError("Zone not found")
        return rc
