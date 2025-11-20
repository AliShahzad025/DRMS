# repositories/base_repository.py
from db.connection import Database

class BaseRepository:
    def __init__(self, db: Database, table_name: str):
        self.db = db
        self.table = table_name

    def fetch_all(self, select="*"):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(f"SELECT {select} FROM {self.table}")
        return cursor.fetchall()

    def fetch_by_id(self, id_col: str, id_val):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM {self.table} WHERE {id_col} = %s", (id_val,))
        return cursor.fetchone()

    def delete_by_id(self, id_col: str, id_val):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {self.table} WHERE {id_col} = %s", (id_val,))
        conn.commit()
        return cursor.rowcount
