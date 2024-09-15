from band import Band
from venue import Venue
from concert import Concert

def main():
    # Create a Band instance
    band = Band(id=1, name='cybersecurities', hometown='Kenya')
    
    # Retrieve all concerts for this band
    print("Concerts for the band:")
    concerts = band.get_concerts()
    for concert in concerts:
        print(concert)
    
    # Retrieve all venues for this band
    print("\nVenues for the band:")
    venues = band.get_venues()
    for venue in venues:
        print(venue)
    
    # Add a new concert for the band
    venue_id = 1  # Assuming venue with ID 1 exists
    date = '2024-10-01'
    band.play_in_venue(venue_id, date)
    print("\nAdded a new concert for the band.")
    
    # Retrieve all introductions for this band
    print("\nAll introductions for the band:")
    introductions = band.get_all_introductions()
    for introduction in introductions:
        print(introduction)
    
    # Find the band with the most performances
    print("\nBand with the most performances:")
    most_performances_band = Band.get_band_with_most_performances()
    print(most_performances_band)
    
    # Create a Venue instance
    venue = Venue(id=1, title='Programming', city='Kenya')
    
    # Retrieve all concerts at this venue
    print("\nConcerts at the venue:")
    concerts_at_venue = venue.get_concerts()
    for concert in concerts_at_venue:
        print(concert)
    
    # Retrieve all bands that have performed at this venue
    print("\nBands that have performed at the venue:")
    bands_at_venue = venue.get_bands()
    for band in bands_at_venue:
        print(band)
    
    # Find a concert at this venue on a specific date
    date = '2024-10-01'
    print(f"\nConcert at the venue on {date}:")
    concert_on_date = venue.get_concert_on_date(date)
    print(concert_on_date)
    
    # Find the most frequent band at this venue
    print("\nMost frequent band at the venue:")
    most_frequent_band = venue.get_most_frequent_band()
    print(most_frequent_band)
    
    # Create a Concert instance
    concert = Concert(id=1, band_id=1, venue_id=1, date='2024-10-01')
    
    # Example: Retrieve the band for this concert
    print("\nBand for the concert:")
    band_for_concert = Concert.get_band(concert.id)
    print(band_for_concert)
    
    #Retrieve the venue for this concert
    print("\nVenue for the concert:")
    venue_for_concert = Concert.get_venue(concert.id)
    print(venue_for_concert)
    
    # to Check if the concert is a hometown show
    print("\nIs the concert a hometown show?")
    is_hometown_show = concert.is_hometown_show()
    print(is_hometown_show)
    
    # Get the introduction for the concert
    print("\nIntroduction for the concert:")
    introduction = concert.introduction()
    print(introduction)

if __name__ == '__main__':
    main()
