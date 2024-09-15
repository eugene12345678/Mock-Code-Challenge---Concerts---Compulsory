# Concert Management System
## Overview
The Concert Management System is a Python-based application designed to manage concerts, bands, and venues using SQLite as the database backend. This system allows users to manage and query data related to concerts, including band performances, venue details, and concert introductions.

## Features
- **Manage Bands:** Add, update, and retrieve information about bands.
- **Manage Venues:** Add, update, and retrieve details about concert venues.
- **Manage Concerts:** Add concerts, link bands and venues, and check concert details.
- **Queries:**
  - Retrieve all concerts for a specific band.
  - Find all venues where a band has performed.
  - Check if a concert is a "hometown show."
  - Get all introductions for a band's concerts.
  - Find the band with the most performances.
  - Retrieve concerts for a specific venue.
  - Get bands that have performed at a venue.
  - Find the most frequent band at a venue.
  - Retrieve details of a concert’s band and venue.

## Setup

### Prerequisites
- Python 3.x
- SQLite3

### Installation
1. **Clone the Repository**

```bash
git clone https://github.com/eugene12345678/Mock-Code-Challenge---Concerts---Compulsory.git
```
2. **Navigate to the Project Directory**

```bash
cd Mock-Code-Challenge-Concerts-Compulsory
```
3 **Create the SQLite Database**

Ensure you have a `concerts.db` SQLite database file. If it doesn't exist, create it by running the provided SQL commands:

```sql
-- Create the bands table
CREATE TABLE bands (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    hometown TEXT NOT NULL
);

-- Create the venues table
CREATE TABLE venues (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    city TEXT NOT NULL
);

-- Create the concerts table
CREATE TABLE concerts (
    id INTEGER PRIMARY KEY,
    band_id INTEGER,
    venue_id INTEGER,
    date TEXT,
    FOREIGN KEY (band_id) REFERENCES bands(id),
    FOREIGN KEY (venue_id) REFERENCES venues(id)
);
```
4. **Install Required Packages**

If you need to install any additional Python packages, you can use:

```bash
pip install -r requirements.txt
```

## Usage
Commit: Added example usage script to demonstrate functionality
1. **Run the Example Script**

To see how the system works, you can run the provided example usage script:
```bash
python3 main.py
```
This script demonstrates various functionalities such as adding concerts, retrieving band details, and checking venue information.
2. **Interact with the Classes**

You can import and use the classes in your Python scripts:
```python
from band import Band
from concert import Concert
from venue import Venue

# Example usage:
band = Band(id=1, name='Cybersecurities', hometown='Kenya')
concerts = band.get_concerts()
print(concerts)
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

