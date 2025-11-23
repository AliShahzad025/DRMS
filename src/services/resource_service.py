from models.resource import ResourceType, ResourceStock

class ResourceService:
    def __init__(self, repo):
        self.repo = repo

    # ----------------------
    # ResourceType methods
    # ----------------------
    def get_all_types(self):
        return self.repo.fetch_all_types()

    def get_type(self, type_id):
        t = self.repo.fetch_type_by_id(type_id)
        if not t:
            raise ValueError("ResourceType not found")
        return t

    def create_type(self, payload):
        return self.repo.create_type(payload)

    def update_type(self, type_id, payload):
        if not self.repo.update_type(type_id, payload):
            raise ValueError("ResourceType not found or no changes")

    def delete_type(self, type_id):
        if not self.repo.delete_type(type_id):
            raise ValueError("ResourceType not found")

    # ----------------------
    # ResourceStock methods
    # ----------------------
    def get_all_resources(self):
        return self.repo.fetch_all_resources()

    def get_resource(self, resource_id):
        r = self.repo.fetch_resource_by_id(resource_id)
        if not r:
            raise ValueError("Resource not found")
        return r

    def create_resource(self, payload):
        return self.repo.create_resource(payload)

    def update_resource(self, resource_id, payload):
        if not self.repo.update_resource(resource_id, payload):
            raise ValueError("Resource not found")

    def delete_resource(self, resource_id):
        if not self.repo.delete_resource(resource_id):
            raise ValueError("Resource not found")

    # ----------------------
    # Actions
    # ----------------------
    def add_stock(self, resource_id, payload):
        self.repo.add_stock(resource_id, payload)

    def update_stock(self, resource_id, payload):
        self.repo.update_stock(resource_id, payload)

    def transfer_resource(self, resource_id, payload):
        self.repo.transfer_resource(resource_id, payload)

    def allocate_resource(self, resource_id, payload):
        self.repo.allocate_resource(resource_id, payload)
