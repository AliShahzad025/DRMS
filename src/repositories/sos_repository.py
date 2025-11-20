# repositories/sos_repository.py
from repositories.base_repository import BaseRepository
from db.connection import Database
from models.sos_request import SOSRequest

class SOSRepository(BaseRepository):
    def __init__(self, db: Database):
        super().__init__(db, "SOSRequest")

    def get_all_requests(self):
        rows = self.fetch_all()
        return [SOSRequest(**r) for r in rows]

    def get_by_id(self, r_id):
        row = self.fetch_by_id("requestID", r_id)
        return SOSRequest(**row) if row else None

    def create_request(self, data):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        sql = """INSERT INTO SOSRequest (victimID, location, latitude, longitude, typeOfNeed, description, urgencyLevel, status, assignedVolunteerID, assignedNGO)
                 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        cursor.execute(sql, (
            data["victimID"], data.get("location"), data.get("latitude"), data.get("longitude"),
            data.get("typeOfNeed"), data.get("description"), data.get("urgencyLevel", "low"),
            data.get("status", "pending"), data.get("assignedVolunteerID"), data.get("assignedNGO")
        ))
        conn.commit()
        return cursor.lastrowid

    def update_request(self, r_id, data):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        sql = """UPDATE SOSRequest SET location=%s, latitude=%s, longitude=%s, typeOfNeed=%s,
                 description=%s, urgencyLevel=%s, status=%s, assignedVolunteerID=%s, assignedNGO=%s
                 WHERE requestID=%s"""
        cursor.execute(sql, (
            data.get("location"), data.get("latitude"), data.get("longitude"),
            data.get("typeOfNeed"), data.get("description"), data.get("urgencyLevel"),
            data.get("status"), data.get("assignedVolunteerID"), data.get("assignedNGO"), r_id
        ))
        conn.commit()
        return cursor.rowcount

    def set_priority_scores(self):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        # call the stored procedure defined in your SQL file
        cursor.execute("CALL compute_priorities()")
        conn.commit()
