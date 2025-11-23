# repositories/resource_repository.py
from models.resource import ResourceType, ResourceStock

class ResourceRepository:
    def __init__(self, db):
        self.db = db

    # -----------------------------
    # ResourceType CRUD Operations
    # -----------------------------
    def fetch_all_types(self):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM ResourceType")
        rows = cursor.fetchall()
        cursor.close()
        return [ResourceType(**r) for r in rows]

    def fetch_type_by_id(self, type_id):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM ResourceType WHERE resourceTypeID=%s", (type_id,))
        row = cursor.fetchone()
        cursor.close()
        return ResourceType(**row) if row else None

    def create_type(self, data):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO ResourceType (name, unit, description) VALUES (%s, %s, %s)",
            (data.get("name"), data.get("unit"), data.get("description"))
        )
        conn.commit()
        rid = cursor.lastrowid
        cursor.close()
        return rid

    def update_type(self, type_id, data):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE ResourceType SET name=%s, unit=%s, description=%s WHERE resourceTypeID=%s",
            (data.get("name"), data.get("unit"), data.get("description"), type_id)
        )
        conn.commit()
        rowcount = cursor.rowcount
        cursor.close()
        return rowcount

    def delete_type(self, type_id):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM ResourceType WHERE resourceTypeID=%s", (type_id,))
        conn.commit()
        rowcount = cursor.rowcount
        cursor.close()
        return rowcount

    # -----------------------------
    # ResourceStock CRUD Operations
    # -----------------------------
    def fetch_all_resources(self):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM ResourceStock")
        rows = cursor.fetchall()
        cursor.close()
        return [ResourceStock(**r) for r in rows]

    def fetch_resource_by_id(self, resource_id):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM ResourceStock WHERE resourceID=%s", (resource_id,))
        row = cursor.fetchone()
        cursor.close()
        return ResourceStock(**row) if row else None

    def create_resource(self, data):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO ResourceStock (resourceTypeID, donorNGO, quantity, status, lastVerifiedBy, location, latitude, longitude)
               VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""",
            (
                data.get("resourceTypeID"), data.get("donorNGO"), data.get("quantity"),
                data.get("status"), data.get("lastVerifiedBy"), data.get("location"),
                data.get("latitude"), data.get("longitude")
            )
        )
        conn.commit()
        rid = cursor.lastrowid
        cursor.close()
        return rid

    def update_resource(self, resource_id, data):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE ResourceStock SET quantity=%s, status=%s, lastVerifiedBy=%s, location=%s WHERE resourceID=%s",
            (data.get("quantity"), data.get("status"), data.get("lastVerifiedBy"), data.get("location"), resource_id)
        )
        conn.commit()
        rc = cursor.rowcount
        cursor.close()
        return rc

    def delete_resource(self, resource_id):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM ResourceStock WHERE resourceID=%s", (resource_id,))
        conn.commit()
        rc = cursor.rowcount
        cursor.close()
        return rc

    # -----------------------------
    # Specialized Resource Actions
    # -----------------------------
    def add_stock(self, resource_id, data):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO ResourceAdd (resourceID, addedBy, quantity, note) VALUES (%s,%s,%s,%s)",
            (resource_id, data.get("addedBy"), data.get("quantity"), data.get("note"))
        )
        conn.commit()
        cursor.close()

    def update_stock(self, resource_id, data):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO ResourceUpdate (resourceID, updatedBy, previousQuantity, newQuantity, note) VALUES (%s,%s,%s,%s,%s)",
            (resource_id, data.get("updatedBy"), data.get("previousQuantity"), data.get("newQuantity"), data.get("note"))
        )
        conn.commit()
        cursor.close()

    def transfer_resource(self, resource_id, data):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO ResourceTransfer (resourceID, fromNGO, toNGO, fromLocation, toLocation, quantity, status, transferredBy)
               VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""",
            (
                resource_id, data.get("fromNGO"), data.get("toNGO"), data.get("fromLocation"),
                data.get("toLocation"), data.get("quantity"), data.get("status","pending"), data.get("transferredBy")
            )
        )
        conn.commit()
        cursor.close()

    def allocate_resource(self, resource_id, data):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO ResourceAllocation (resourceID, allocatedToType, allocatedToID, requestID, quantity, allocationStatus)
               VALUES (%s,%s,%s,%s,%s,%s)""",
            (
                resource_id, data.get("allocatedToType"), data.get("allocatedToID"), data.get("requestID"),
                data.get("quantity"), data.get("allocationStatus","pending")
            )
        )
        conn.commit()
        cursor.close()
