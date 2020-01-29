# Waarnemingen boten

This project is part of the waarnemingen cluster. All data related to boats should be imported and exposed here through an API (API not yet implemented). 

# Waternet

Currently Waternet is the only datasource we are retrieving data from. We retrieve AIS (automatic identification system) data from ships around Amsterdam, at a specific bounding box, every x amount of minutes.

## Getting started

Start the database

```docker-compose up -d database```


To scrape the waternet API locally first add the user credentials in your `src/.env` file like so:

```
WATERNET_USERNAME=<username>
WATERNET_PASSWORD=<password>
```

Then run the script through docker

```
docker-compose run job python manage.py scrape_waternet
```

Now you have a snapshot of the api at the moment the script ran.
To import (unpack) the snapshot run the import script:

```
docker-compose run job python manage.py import_waternet
```