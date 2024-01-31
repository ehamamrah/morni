# MORNI

## Stack
* Django 5.0.1
* Django DRF
* GeoDjango
* Docker
* PostGIS

## Why PostGIS?
We need a DB engine that makes it easy to handle geofences, And since we are working with Geodjango, it's compitable with PostGIS to handle storing, indexing and querying geo data.

## Run the project
* Go to directory of the project
* Run ```make image``` to build the image
* Generate .env file and add ```DB_NAME, DB_USER, DB_PASS, DB_HOST``` to it.
* Run Server & DB Container using command ```make dev-run```
* To run any migrations use ```make migrate```

```If server failed to connect to db, run make dev-run again```

## Importing Data
* Go to directory of the project
* Run ```make import-data``` and it will run the task
