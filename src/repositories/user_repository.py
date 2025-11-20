from db.connection import Database
from models.user import User

class UserRepository:
    def __init__(self, db: Database):
        self.db = db

    def get_all_users(self):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM UserAccount")
        results = cursor.fetchall()
        return [User(**row) for row in results]

    def get_user_by_id(self, user_id):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM UserAccount WHERE userID = %s", (user_id,))
        row = cursor.fetchone()
        if row:
            return User(**row)
        return None

    def create_user(self, user: User):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        query = """
        INSERT INTO UserAccount (name, email, phone, location, latitude, longitude, language, role, password_hash)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        cursor.execute(query, (user.name, user.email, user.phone, user.location,
                               user.latitude, user.longitude, user.language, user.role, user.password_hash))
        conn.commit()
        user.userID = cursor.lastrowid
        return user

    def delete_user(self, user_id):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM UserAccount WHERE userID = %s", (user_id,))
        conn.commit()
        return cursor.rowcount > 0
