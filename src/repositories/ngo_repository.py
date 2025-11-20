# repositories/ngo_repository.py
from repositories.base_repository import BaseRepository
from db.connection import Database
from models.ngo import NGO

class NGORepository(BaseRepository):
    def __init__(self, db: Database):
        super().__init__(db, "NGO")

    def get_all_ngos(self):
        rows = self.fetch_all()
        return [NGO(**r) for r in rows]

    def get_ngo_by_id(self, ngo_id):
        row = self.fetch_by_id("ngoID", ngo_id)
        return NGO(**row) if row else None

    def create_ngo(self, data: dict):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        sql = """INSERT INTO NGO (ngoID, orgName, verified, registration_doc, region, contact_person)
                 VALUES (%s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, (
            data.get("ngoID"),
            data["orgName"],
            data.get("verified", False),
            data.get("registration_doc"),
            data.get("region"),
            data.get("contact_person"),
        ))
        conn.commit()
        return cursor.lastrowid

    def update_ngo(self, ngo_id, data: dict):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        sql = """UPDATE NGO SET orgName=%s, verified=%s, registration_doc=%s, region=%s, contact_person=%s
                 WHERE ngoID=%s"""
        cursor.execute(sql, (
            data.get("orgName"),
            data.get("verified"),
            data.get("registration_doc"),
            data.get("region"),
            data.get("contact_person"),
            ngo_id
        ))
        conn.commit()
        return cursor.rowcount
