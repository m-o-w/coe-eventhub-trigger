# Azure Function for Event Hub Trigger and MongoDB Integration

This project implements an Azure Function that triggers on new events published to an Azure Event Hub. It processes the JSON content from these events and inserts the data into a MongoDB collection.

## Project Structure

- **app_config_manager.py**: Handles retrieval of configuration values from Azure App Configuration.
- **mongo_operations.py**: Contains the logic to insert JSON data into MongoDB.
- **function_app.py**: The main Azure Function that triggers on Event Hub events, processes the event data, and inserts it into MongoDB.
- **local.settings.json**: Stores local environment settings for development purposes.
- **requirements.txt**: Lists all dependencies for the project.

## Environmental Variables

Ensure the following environment variables are set in your Azure Function App settings:

- **EventHubRootManageSharedAccessKey_FOREX_EVENTHUB_TRIGGER**: The connection string for your Azure Event Hub.
  - Example: `Endpoint=sb://coe-eventhub-ns.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=your_event_hub_key`
- **EVENT_HUB_NAME_FOREX_EVENTHUB_TRIGGER**: The name of the Event Hub to monitor.
  - Example: `coe-eventhub-01`
- **AZURE_APP_CONFIG_CONNECTION_STRING**: The connection string for your Azure App Configuration.
  - Example: `Endpoint=https://coe-appconfig.azconfig.io;Id=your_id;Secret=your_secret`

## Azure App Configuration Variables

Add the following variables to your Azure App Configuration:

- **MongoUri_ClientAPI**: The connection string for your MongoDB instance.
  - Example: `mongodb+srv://username:password@cluster0.mongodb.net/?retryWrites=true&w=majority&appName=your_app_name`

## How It Works

1. **Event Hub Trigger**: The Azure Function is triggered whenever a new event is published to the specified Event Hub.
2. **Process Event Data**: The function reads and parses the JSON content from the event data.
3. **Insert into MongoDB**: The parsed JSON data is inserted into the specified MongoDB collection.

## Dependencies

Ensure you have the following dependencies listed in `requirements.txt`:

- `azure-functions`
- `azure-eventhub`
- `azure-identity`
- `azure-appconfiguration`
- `pymongo`