# ETL_project

* Target
  - Check out how many rockets launched so far, and how many rockets are going to be launched.
  - Make a API server to provide the information

* Data collection
  - Data scraped from different three web pages (scrape.py)
  - https://nextspaceflight.com/launches/past/, https://nextspaceflight.com/launches/ and https://nextspaceflight.com/rockets/
  - Beautifulsoup and splinter used

* Database
  - Stored data to MongoDB (data_into_db.py)
  - I believe NoSQL is more suitable to store web scraped data because there are huge amount of data.

* API Server
  - Flask web server (app.py)

* Data analysis
  - Rocket.ipnyb
  - convert.py - Convert strings to integer values