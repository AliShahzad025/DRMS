from repositories.user_repository import UserRepository
from models.user import User

class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def get_all_users(self):
        users = self.user_repo.get_all_users()
        return users

    def get_user_by_id(self, user_id: int):
        user = self.user_repo.get_user_by_id(user_id)
        if not user:
            raise ValueError(f"User with ID {user_id} not found")
        return user

    def create_user(self, user_data: dict):
        # Simple validation
        if "email" not in user_data or "role" not in user_data:
            raise ValueError("Missing required fields: email or role")

        user = User(**user_data)
        created_user = self.user_repo.create_user(user)
        return created_user

    def delete_user(self, user_id: int):
        deleted = self.user_repo.delete_user(user_id)
        if not deleted:
            raise ValueError(f"User with ID {user_id} not found or already deleted")
        return True
