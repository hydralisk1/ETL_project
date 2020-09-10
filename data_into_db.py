import pymongo
from scrape import scrape_past, scrape_upcoming, scrape_rocket

conn = "mongodb://localhost:27017"
with pymongo.MongoClient(conn) as client:
    db = client.spaceship

    # If the DB has data, drop all collections
    db.past.drop()
    db.upcoming.drop()
    db.rocket.drop()

    # Insert data into the DB
    db.past.insert_many(scrape_past(), ordered=False)
    db.upcoming.insert_many(scrape_upcoming(), ordered=False)
    db.rocket.insert_many(scrape_rocket(), ordered=False)