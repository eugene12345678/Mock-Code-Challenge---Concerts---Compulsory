
import sqlite3

class Band:
    def __init__(self, id, name, hometown):
        self.id = id
        self.name = name
        self.hometown = hometown

    def get_concerts(self):
        with sqlite3.connect('concerts.db') as connection:
            cursor = connection.cursor()    # Get all concerts for the band
            cursor.execute('''
                SELECT * FROM concerts WHERE band_id = ?;
            ''', (self.id,))
            return cursor.fetchall()

    def get_venues(self):
       with sqlite3.connect('concerts.db') as connection:
            cursor = connection.cursor()    # Get all venues where the band has performed
            cursor.execute('''
                SELECT DISTINCT venues.* FROM venues
                JOIN concerts ON venues.id = concerts.venue_id
                WHERE concerts.band_id = ?;
            ''', (self.id,))
            return cursor.fetchall()

    def play_in_venue(self, venue_id, date):
        with sqlite3.connect('concerts.db') as connection:
            cursor = connection.cursor()     # Add a new concert for the band at a given venue and date
            cursor.execute('''
                INSERT INTO concerts (band_id, venue_id, date) VALUES (?, ?, ?);
            ''', (self.id, venue_id, date))
            connection.commit()

    def get_all_introductions(self):
        with sqlite3.connect('concerts.db') as connection:
            cursor = connection.cursor()     # Get introduction messages for all concerts of the band
            cursor.execute('''
                SELECT venues.city, bands.name, bands.hometown
                FROM concerts
                JOIN venues ON concerts.venue_id = venues.id
                JOIN bands ON concerts.band_id = bands.id
                WHERE concerts.band_id = ?;
            ''', (self.id,))
            rows = cursor.fetchall()
            return [f"Hello {city}!!!!! We are {name} and we're from {hometown}" for city, name, hometown in rows]

    @staticmethod
    def get_band_with_most_performances():
        with sqlite3.connect('concerts.db') as connection:
            cursor = connection.cursor()    # Get the band with the most performances
            cursor.execute('''
                SELECT bands.*, COUNT(concerts.id) AS performance_count
                FROM bands
                JOIN concerts ON concerts.band_id = bands.id
                GROUP BY bands.id
                ORDER BY performance_count DESC
                LIMIT 1;
            ''')
            return cursor.fetchone()
