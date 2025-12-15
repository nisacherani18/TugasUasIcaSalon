from database.db_connection import get_connection

class Booking:
    def __init__(self, user_id=None, service_id=None, booking_date=None):
        self.user_id = user_id
        self.service_id = service_id
        self.booking_date = booking_date

    def add_booking(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO bookings (user_id, service_id, booking_date) VALUES (%s, %s, %s)",
            (self.user_id, self.service_id, self.booking_date)
        )
        conn.commit()
        conn.close()
