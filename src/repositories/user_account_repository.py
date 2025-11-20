# repositories/user_account_repository.py

from models.user_account import UserAccount
from db.connection import Database

class UserAccountRepository:
    def __init__(self, db: Database):
        self.db = db

    def get_all(self):
        conn = self.db.get_connection()
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM UserAccount")
            rows = cursor.fetchall()
            return [UserAccount(**row) for row in rows]
        finally:
            cursor.close()
            conn.close()

    def get_by_id(self, user_id):
        conn = self.db.get_connection()
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM UserAccount WHERE userID=%s", (user_id,))
            row = cursor.fetchone()
            return UserAccount(**row) if row else None
        finally:
            cursor.close()
            conn.close()

    def get_by_email(self, email):
        conn = self.db.get_connection()
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM UserAccount WHERE email=%s", (email,))
            row = cursor.fetchone()
            return UserAccount(**row) if row else None
        finally:
            cursor.close()
            conn.close()

    def create(self, user: UserAccount):
        conn = self.db.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO UserAccount (name, email, password, phone, role)
                VALUES (%s, %s, %s, %s, %s)
            """, (user.name, user.email, user.password, user.phone, user.role))
            conn.commit()
            return cursor.lastrowid
        finally:
            cursor.close()
            conn.close()

    def update(self, user_id, fields):
        conn = self.db.get_connection()
        try:
            cursor = conn.cursor()
            updates = []
            values = []

            for key, value in fields.items():
                updates.append(f"{key}=%s")
                values.append(value)

            values.append(user_id)
            sql = f"UPDATE UserAccount SET {', '.join(updates)} WHERE userID=%s"
            cursor.execute(sql, values)
            conn.commit()
            return cursor.rowcount > 0
        finally:
            cursor.close()
            conn.close()

    def delete(self, user_id):
        conn = self.db.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM UserAccount WHERE userID=%s", (user_id,))
            conn.commit()
            return cursor.rowcount > 0
        finally:
            cursor.close()
            conn.close()
