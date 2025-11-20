from services.user_services import UserService

class UserController:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def list_users(self):
        users = self.user_service.get_all_users()
        for user in users:
            print(user)

    def get_user(self, user_id):
        try:
            user = self.user_service.get_user_by_id(user_id)
            print("Found:", user)
        except ValueError as e:
            print("", e)

    def add_user(self, user_data):
        try:
            created_user = self.user_service.create_user(user_data)
            print(" Created:", created_user)
        except ValueError as e:
            print("", e)

    def remove_user(self, user_id):
        try:
            self.user_service.delete_user(user_id)
            print(f" Deleted user with ID {user_id}")
        except ValueError as e:
            print("", e)
