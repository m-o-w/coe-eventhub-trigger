import logging
from pymongo import MongoClient

class MongoOperations:
    def __init__(self, mongo_uri, database_name, collection_name):
        self.mongo_uri = mongo_uri
        self.database_name = database_name
        self.collection_name = collection_name
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.database_name]
        self.collection = self.db[self.collection_name]

    def insert_event_payload(self, event_payload):
        try:
            result = self.collection.insert_one({"event_payload": event_payload})
            logging.info('Inserted document ID: %s', result.inserted_id)
            return result.inserted_id
        except Exception as e:
            logging.error(f"Failed to insert document into MongoDB: {e}")
            raise
