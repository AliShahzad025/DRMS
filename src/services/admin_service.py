from repositories.admin_repository import AdminRepository

class AdminService:
    def __init__(self, admin_repo: AdminRepository):
        self.admin_repo = admin_repo

    def list_admins(self):
        return self.admin_repo.get_all_admins()

    def get_admin(self, admin_id):
        admin = self.admin_repo.get_admin_by_id(admin_id)
        if not admin:
            raise ValueError("Admin not found")
        return admin
