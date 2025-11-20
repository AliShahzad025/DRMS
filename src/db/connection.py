import mysql.connector
from mysql.connector import Error
from config import DBConfig

class Database:
    def __init__(self):
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=DBConfig.HOST,
                user=DBConfig.USER,
                password=DBConfig.PASSWORD,
                database=DBConfig.DATABASE
            )
            if self.connection.is_connected():
                print("✅ SUCCESS: Connected to MySQL!")
        except Error as e:
            print(f"❌ Error connecting to MySQL: {e}")
            raise e

    def get_connection(self):
        if not self.connection or not self.connection.is_connected():
            self.connect()
        return self.connection

    def close(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Connection closed.")
