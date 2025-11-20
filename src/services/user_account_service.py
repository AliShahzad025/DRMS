# services/user_account_service.py

import hashlib
from repositories.user_account_repository import UserAccountRepository
from models.user_account import UserAccount

def hash_password(pwd):
    return hashlib.sha256(pwd.encode()).hexdigest()

class UserAccountService:
    def __init__(self, repo: UserAccountRepository):
        self.repo = repo

    def list_users(self):
        return self.repo.get_all()

    def get_user(self, user_id):
        user = self.repo.get_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        return user

    def create_user(self, payload):
        if "email" not in payload:
            raise ValueError("email required")

        existing = self.repo.get_by_email(payload["email"])
        if existing:
            raise ValueError("Email already exists")

        password = hash_password(payload.get("password", ""))

        user = UserAccount(
            name=payload.get("name"),
            email=payload.get("email"),
            password=password,
            phone=payload.get("phone"),
            role=payload.get("role")
        )

        new_id = self.repo.create(user)
        user.userID = new_id
        return user

    def update_user(self, user_id, payload):
        if "password" in payload:
            payload["password"] = hash_password(payload["password"])

        ok = self.repo.update(user_id, payload)
        if not ok:
            raise ValueError("User not updated or not found")

        return self.repo.get_by_id(user_id)

    def delete_user(self, user_id):
        if not self.repo.delete(user_id):
            raise ValueError("User not found")

    def login(self, email, password):
        user = self.repo.get_by_email(email)
        if not user:
            raise ValueError("Invalid email or password")

        hashed = hash_password(password)
        if hashed != user.password:
            raise ValueError("Invalid email or password")

        return user
