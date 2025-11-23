from repositories.base_repository import BaseRepository
from db.connection import Database
from models.victim import Victim

class VictimRepository(BaseRepository):
    def __init__(self, db: Database):
        super().__init__(db, "Victim")

    def get_all_victims(self):
        rows = self.fetch_all()
        return [Victim(**r) for r in rows]

    def get_victim_by_id(self, victim_id):
        row = self.fetch_by_id("victimID", victim_id)
        return Victim(**row) if row else None

    def create_victim(self, data: dict):
        conn = self.db.get_connection()
        cur = conn.cursor()
        sql = "INSERT INTO Victim (victimID, verified_contact, vulnerability_notes) VALUES (%s,%s,%s)"
        cur.execute(sql, (data.get("victimID"), data.get("verified_contact", False), data.get("vulnerability_notes")))
        conn.commit()
        cur.close()
        return cur.lastrowid or data.get("victimID")

    def update_victim(self, victim_id, data: dict):
        conn = self.db.get_connection()
        cur = conn.cursor()
        sql = "UPDATE Victim SET verified_contact=%s, vulnerability_notes=%s WHERE victimID=%s"
        cur.execute(sql, (data.get("verified_contact"), data.get("vulnerability_notes"), victim_id))
        conn.commit()
        rc = cur.rowcount
        cur.close()
        return rc

    def delete_victim(self, victim_id):
        conn = self.db.get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM Victim WHERE victimID=%s", (victim_id,))
        conn.commit()
        rc = cur.rowcount
        cur.close()
        return rc
