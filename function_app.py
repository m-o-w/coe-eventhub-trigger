import os
import azure.functions as func
import logging
import json
from app_config_manager import AppConfigManager  # Assuming your class is in a file named app_config_manager.py
from mongo_operations import MongoOperations  # Import the new MongoOperations class

logging.info('------------Start of Function App------------')
app = func.FunctionApp()

@app.function_name(name="coe_eventhub_forex_trigger")
@app.event_hub_message_trigger(arg_name="azeventhub", 
                               event_hub_name=os.getenv("EVENT_HUB_NAME_FOREX_EVENTHUB_TRIGGER"), 
                               connection="EventHubRootManageSharedAccessKey_FOREX_EVENTHUB_TRIGGER")
def forex_eventhub_trigger(azeventhub: func.EventHubEvent):
    logging.info('Python EventHub trigger processed an event: %s', azeventhub.get_body().decode('utf-8'))
    
    try:
        # Set up AppConfigManager with the connection string from environment variable
        app_config_manager = AppConfigManager()

        # Retrieve configuration values from Azure App Configuration
        mongo_uri = app_config_manager.get_configuration_value("MongoUri_FOREX_EVENTHUB_TRIGGER")
        database_name = app_config_manager.get_configuration_value("DatabaseName_FOREX_EVENTHUB_TRIGGER")
        collection_name = app_config_manager.get_configuration_value("CollectionName_FOREX_EVENTHUB_TRIGGER")
        
        # Log retrieved configuration values
        logging.info(f"Retrieved MongoUri: {mongo_uri}")
        logging.info(f"Retrieved DatabaseName: {database_name}")
        logging.info(f"Retrieved CollectionName: {collection_name}")
        
        if not mongo_uri:
            raise ValueError("MongoDB URI is not configured in Azure App Configuration.")
        
        if not database_name:
            raise ValueError("MongoDB Database name is not configured in Azure App Configuration.")
        
        if not collection_name:
            raise ValueError("MongoDB Collection name is not configured in Azure App Configuration.")

        # Parse the event payload
        event_payload = azeventhub.get_body().decode('utf-8')
        
        # Print the JSON payload
        try:
            event_payload_json = json.loads(event_payload)
            logging.info('Event payload JSON: %s', json.dumps(event_payload_json, indent=2))
        except json.JSONDecodeError:
            logging.error('Failed to decode event payload as JSON.')

        # Initialize MongoOperations
        mongo_ops = MongoOperations(mongo_uri, database_name, collection_name)
        
        # Insert the event payload into the collection
        mongo_ops.insert_event_payload(event_payload)

    except Exception as e:
        logging.error(f"Error processing the event hub trigger: {e}")
        raise
