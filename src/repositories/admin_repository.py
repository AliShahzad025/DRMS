from db.connection import Database
from models.admin import Admin

class AdminRepository:
    def __init__(self, db: Database):
        self.db = db

    def get_all_admins(self):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Admin")
        return [Admin(**row) for row in cursor.fetchall()]

    def get_admin_by_id(self, admin_id):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Admin WHERE adminID = %s", (admin_id,))
        row = cursor.fetchone()
        return Admin(**row) if row else None
