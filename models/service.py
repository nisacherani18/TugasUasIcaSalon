from database.db_connection import get_connection

class Service:
    def __init__(self):
        pass

    def show_services(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM services")
        data = cursor.fetchall()
        conn.close()
        return data
