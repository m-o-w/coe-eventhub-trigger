# Function App

## Summary
This Azure Function App is designed to process messages from an Event Hub. It uses a trigger to listen for incoming messages and processes them accordingly.

## External Dependencies
The following external libraries are required for this function app:
- `azure-functions`: For creating and managing Azure Functions.
- `pymongo`: For connecting to and interacting with MongoDB.
- `app_config`: Custom module to fetch application configuration values.

## Environmental Variables
The function app requires the following environmental variables to be set:
- `EVENT_HUB_NAME`: The name of the Event Hub to listen to.
- `EVENT_HUB_ROOT_MANAGE_SHARED_ACCESS_KEY`: The connection string for the Event Hub.
- `MONGO_URI`: The URI for connecting to the MongoDB instance.
- `DATABASE_NAME`: The name of the MongoDB database.
- `COLLECTION_NAME`: The name of the MongoDB collection.

## App Config Variables
The function app fetches the following configuration values using the `get_app_config_values` function from the `app_config` module:
- `EVENT_HUB_NAME`
- `EVENT_HUB_ROOT_MANAGE_SHARED_ACCESS_KEY`
- `MONGO_URI`
- `DATABASE_NAME`
- `COLLECTION_NAME`