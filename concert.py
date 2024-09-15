
import sqlite3

class Concert:
    def __init__(self, id, band_id, venue_id, date):
        self.id = id
        self.band_id = band_id
        self.venue_id = venue_id
        self.date = date

    @staticmethod
    def get_band(concert_id):
        with sqlite3.connect('concerts.db') as connection:
            cursor = connection.cursor()     # Retrieve the band associated with the given concert ID
            cursor.execute('''
                SELECT * FROM bands 
                WHERE id = (SELECT band_id FROM concerts WHERE id = ?);
            ''', (concert_id,))
            return cursor.fetchone()

    @staticmethod
    def get_venue(concert_id):
        with sqlite3.connect('concerts.db') as connection:
            cursor = connection.cursor()          # Retrieve the venue associated with the given concert ID
            cursor.execute('''
                SELECT * FROM venues 
                WHERE id = (SELECT venue_id FROM concerts WHERE id = ?);
            ''', (concert_id,))
            return cursor.fetchone()

    def is_hometown_show(self):
        with sqlite3.connect('concerts.db') as connection:
            cursor = connection.cursor()        # Check if the concert is a hometown show
            cursor.execute('''
                SELECT COUNT(*) FROM concerts
                JOIN bands ON concerts.band_id = bands.id
                JOIN venues ON concerts.venue_id = venues.id
                WHERE concerts.id = ? AND bands.hometown = venues.city;
            ''', (self.id,))
            result = cursor.fetchone()
            return result[0] > 0

    def introduction(self):
       with sqlite3.connect('concerts.db') as connection:
            cursor = connection.cursor()       # Provide an introduction message for the concert
            cursor.execute('''
                SELECT venues.city, bands.name, bands.hometown
                FROM concerts
                JOIN bands ON concerts.band_id = bands.id
                JOIN venues ON concerts.venue_id = venues.id
                WHERE concerts.id = ?;
            ''', (self.id,))
            venue_city, band_name, band_hometown = cursor.fetchone()
            return f"Hello {venue_city}!!!!! We are {band_name} and we're from {band_hometown}"
