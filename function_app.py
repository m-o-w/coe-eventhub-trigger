import os
import azure.functions as func
import logging
import json
import uuid
from app_config_manager import AppConfigManager
from mongo_operations import MongoOperations

request_id = str(uuid.uuid4())
interface_id = "INTSVC114_MOCKAPI"
log_prefix = f"{interface_id} [{request_id}]"

logging.info(f'{log_prefix}: ------------Start of Function App------------')
app = func.FunctionApp()

@app.function_name(name="coe_eventhub_forex_trigger")
@app.event_hub_message_trigger(arg_name="azeventhub", 
                               event_hub_name=os.getenv("EVENT_HUB_NAME_FOREX_EVENTHUB_TRIGGER"), 
                               connection="EventHubRootManageSharedAccessKey_FOREX_EVENTHUB_TRIGGER")
def forex_eventhub_trigger(azeventhub: func.EventHubEvent):
    logging.info(f'{log_prefix}: Python EventHub trigger processed an event: {azeventhub.get_body().decode("utf-8")}')
    
    try:
        app_config_manager = AppConfigManager()
        mongo_uri = app_config_manager.get_configuration_value("MongoUri_FOREX_EVENTHUB_TRIGGER")
        database_name = app_config_manager.get_configuration_value("DatabaseName_FOREX_EVENTHUB_TRIGGER")
        collection_name = app_config_manager.get_configuration_value("CollectionName_FOREX_EVENTHUB_TRIGGER")
        
        logging.info(f'{log_prefix}: Retrieved MongoUri: {mongo_uri}')
        logging.info(f'{log_prefix}: Retrieved DatabaseName: {database_name}')
        logging.info(f'{log_prefix}: Retrieved CollectionName: {collection_name}')
        
        if not mongo_uri:
            raise ValueError(f'{log_prefix}: MongoDB URI is not configured in Azure App Configuration.')
        
        if not database_name:
            raise ValueError(f'{log_prefix}: MongoDB Database name is not configured in Azure App Configuration.')
        
        if not collection_name:
            raise ValueError(f'{log_prefix}: MongoDB Collection name is not configured in Azure App Configuration.')
        
        event_payload = azeventhub.get_body().decode('utf-8')
        
        try:
            event_payload_json = json.loads(event_payload)
            logging.info(f'{log_prefix}: Event payload JSON: {json.dumps(event_payload_json, indent=2)}')
        except json.JSONDecodeError:
            logging.error(f'{log_prefix}: Failed to decode event payload as JSON.')
        
        logging.info(f'{log_prefix}: Inserting event payload into MongoDB: {event_payload}')
        mongo_ops = MongoOperations(mongo_uri, database_name, collection_name)
        mongo_ops.insert_event_payload(event_payload)
    except Exception as e:
        logging.error(f'{log_prefix}: Error processing event: {e}')