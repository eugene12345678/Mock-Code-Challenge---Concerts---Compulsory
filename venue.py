
import sqlite3

class Venue:
    def __init__(self, id, title, city):
        self.id = id
        self.title = title
        self.city = city

    def get_concerts(self):
        with sqlite3.connect('concerts.db') as connection:
            cursor = connection.cursor()   # Get all concerts at this venue
            cursor.execute('''
                SELECT * FROM concerts WHERE venue_id = ?;
            ''', (self.id,))
            return cursor.fetchall()

    def get_bands(self):
        with sqlite3.connect('concerts.db') as connection:
            cursor = connection.cursor()    # Get all bands that have performed at this venue
            cursor.execute('''
                SELECT DISTINCT bands.* FROM bands
                JOIN concerts ON bands.id = concerts.band_id
                WHERE concerts.venue_id = ?;
            ''', (self.id,))
            return cursor.fetchall()

    def get_concert_on_date(self, date):
        with sqlite3.connect('concerts.db') as connection:
            cursor = connection.cursor()    # Get a concert at this venue on a specific date
            cursor.execute('''
                SELECT * FROM concerts WHERE venue_id = ? AND date = ?;
            ''', (self.id, date))
            return cursor.fetchone()

    def get_most_frequent_band(self):
        with sqlite3.connect('concerts.db') as connection:
            cursor = connection.cursor()     # Get the band that has performed the most at this venue
            cursor.execute('''
                SELECT bands.*, COUNT(concerts.id) AS performance_count
                FROM bands
                JOIN concerts ON concerts.band_id = bands.id
                WHERE concerts.venue_id = ?
                GROUP BY bands.id
                ORDER BY performance_count DESC
                LIMIT 1;
            ''', (self.id,))
            return cursor.fetchone()
