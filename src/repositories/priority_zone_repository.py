from repositories.base_repository import BaseRepository
from db.connection import Database
from models.priority_zone import PriorityZone

class PriorityZoneRepository(BaseRepository):
    def __init__(self, db: Database):
        super().__init__(db, "PriorityZone")

    def get_all_zones(self):
        rows = self.fetch_all()
        return [PriorityZone(**r) for r in rows]

    def get_zone(self, zone_id):
        row = self.fetch_by_id("zoneID", zone_id)
        return PriorityZone(**row) if row else None

    def create_zone(self, data: dict):
        conn = self.db.get_connection()
        cur = conn.cursor()
        sql = """INSERT INTO PriorityZone (name, description, centerLat, centerLong, radius_km, priority_level)
                 VALUES (%s,%s,%s,%s,%s,%s)"""
        cur.execute(sql, (data.get("name"), data.get("description"), data.get("centerLat"), data.get("centerLong"), data.get("radius_km"), data.get("priority_level", "medium")))
        conn.commit()
        last = cur.lastrowid
        cur.close()
        return last

    def update_zone(self, zone_id, data: dict):
        conn = self.db.get_connection()
        cur = conn.cursor()
        sql = """UPDATE PriorityZone SET name=%s, description=%s, centerLat=%s, centerLong=%s, radius_km=%s, priority_level=%s WHERE zoneID=%s"""
        cur.execute(sql, (data.get("name"), data.get("description"), data.get("centerLat"), data.get("centerLong"), data.get("radius_km"), data.get("priority_level"), zone_id))
        conn.commit()
        rc = cur.rowcount
        cur.close()
        return rc

    def delete_zone(self, zone_id):
        conn = self.db.get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM PriorityZone WHERE zoneID=%s", (zone_id,))
        conn.commit()
        rc = cur.rowcount
        cur.close()
        return rc
