import logging
import uuid
from pymongo import MongoClient

request_id = str(uuid.uuid4())
interface_id = "INTSVC114_MOCKAPI"
log_prefix = f"{interface_id} [{request_id}]"

class MongoOperations:
    def __init__(self, mongo_uri, database_name, collection_name):
        self.mongo_uri = mongo_uri
        self.database_name = database_name
        self.collection_name = collection_name
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.database_name]
        self.collection = self.db[self.collection_name]
        logging.info(f'{log_prefix}: Initialized MongoOperations with URI: {mongo_uri}, Database: {database_name}, Collection: {collection_name}')

    def insert_event_payload(self, event_payload):
        try:
            result = self.collection.insert_one({"event_payload": event_payload})
            logging.info(f'{log_prefix}: Inserted document ID: {result.inserted_id}')
            return result.inserted_id
        except Exception as e:
            logging.error(f'{log_prefix}: Failed to insert document into MongoDB: {e}')
            raise