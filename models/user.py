from database.db_connection import get_connection

class User:
    def __init__(self, name=None, phone=None):
        self.name = name
        self.phone = phone

    def add_user(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (name, phone) VALUES (%s, %s)",
            (self.name, self.phone)
        )
        conn.commit()
        conn.close()
