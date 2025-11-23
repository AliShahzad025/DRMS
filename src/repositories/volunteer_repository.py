# repositories/volunteer_repository.py

from repositories.base_repository import BaseRepository
from db.connection import Database
from models.volunteer import Volunteer

class VolunteerRepository(BaseRepository):
    def __init__(self, db: Database):
        # BaseRepository stores self.db and self.table
        super().__init__(db, "Volunteer")

    def get_all_volunteers(self):
        rows = self.fetch_all()
        return [Volunteer(**r) for r in rows]

    def get_volunteer_by_id(self, volunteer_id):
        row = self.fetch_by_id("volunteerID", volunteer_id)
        return Volunteer(**row) if row else None

    def create_volunteer(self, data: dict):
        """
        Note: volunteerID in your schema is the same as the userID (one-to-one).
        So client should provide volunteerID = existing userID (or you can create user first elsewhere).
        """
        conn = self.db.get_connection()
        cursor = conn.cursor()
        sql = """INSERT INTO Volunteer (volunteerID, roles, verified, status, last_active)
                 VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(sql, (
            data.get("volunteerID"),
            data.get("roles"),
            data.get("verified", False),
            data.get("status", "available"),
            data.get("last_active")
        ))
        conn.commit()
        last_id = cursor.lastrowid or data.get("volunteerID")
        cursor.close()
        return last_id

    def update_volunteer(self, volunteer_id, data: dict):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        sql = """UPDATE Volunteer
                 SET roles=%s, verified=%s, status=%s, last_active=%s
                 WHERE volunteerID=%s"""
        cursor.execute(sql, (
            data.get("roles"),
            data.get("verified"),
            data.get("status"),
            data.get("last_active"),
            volunteer_id
        ))
        conn.commit()
        rowcount = cursor.rowcount
        cursor.close()
        return rowcount

    def delete_volunteer(self, volunteer_id):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Volunteer WHERE volunteerID = %s", (volunteer_id,))
        conn.commit()
        rowcount = cursor.rowcount
        cursor.close()
        return rowcount
