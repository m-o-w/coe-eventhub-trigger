import os
import azure.functions as func
import logging
from app_config import get_app_config_values
from pymongo import MongoClient

logging.info('------------Start of Function App------------')
app = func.FunctionApp()

logging.info('Getting app config values')
EVENT_HUB_NAME, EVENT_HUB_ROOT_MANAGE_SHARED_ACCESS_KEY, MONGO_URI, DATABASE_NAME, COLLECTION_NAME = get_app_config_values()

@app.function_name(name="coe_eventhub_forex_trigger")
@app.event_hub_message_trigger(arg_name="azeventhub", event_hub_name=EVENT_HUB_NAME,
                               connection=EVENT_HUB_ROOT_MANAGE_SHARED_ACCESS_KEY)
def coe_eventhub_forex_trigger(azeventhub: func.EventHubEvent):
    logging.info('Python EventHub trigger processed an event: %s',
                 azeventhub.get_body().decode('utf-8'))
    
    # Parse the event payload
    event_payload = azeventhub.get_body().decode('utf-8')
    
    # Connect to MongoDB
    client = MongoClient(MONGO_URI)
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]
    
    # Insert the event payload into the collection
    result = collection.insert_one({"event_payload": event_payload})
    logging.info('Inserted document ID: %s', result.inserted_id)
