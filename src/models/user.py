class User:
    def __init__(self, userID=None, name=None, email=None, phone=None, location=None,
                 latitude=None, longitude=None, language='en', role=None, password_hash=None,
                 createdAt=None, updatedAt=None):
        self.userID = userID
        self.name = name
        self.email = email
        self.phone = phone
        self.location = location
        self.latitude = latitude
        self.longitude = longitude
        self.language = language
        self.role = role
        self.password_hash = password_hash
        self.createdAt = createdAt
        self.updatedAt = updatedAt

    def __repr__(self):
        return f"<User {self.userID}: {self.name}, {self.role}>"
