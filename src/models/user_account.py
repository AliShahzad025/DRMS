# models/user_account.py

class UserAccount:
    def __init__(self, userID=None, name=None, email=None, password=None, phone=None, role=None):
        self.userID = userID
        self.name = name
        self.email = email
        self.password = password  # hashed
        self.phone = phone
        self.role = role

    def to_dict(self):
        return {
            "userID": self.userID,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "role": self.role
            # password intentionally excluded
        }
