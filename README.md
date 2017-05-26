# Hacker News

This web application scrapes Hacker News and saves/updates 
all of the items into a Postgres Database.

Scraping hackernews can been done through the command line with the command -
python manage.py scrape.

This command is set to run every 10 minutes through use of the Heroku Scheduler.

To view this application go to https://scrapernews.herokuapp.com/