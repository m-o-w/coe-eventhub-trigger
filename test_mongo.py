from pymongo import MongoClient
import json

# MongoDB connection details
MONGO_URI = "mongodb+srv://mowadmin:mowadmin@cluster0.u0yhqex.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DATABASE_NAME = "sape-coe"
COLLECTION_NAME = "forex"

# Dummy JSON payload
dummy_payload = {
    "currency": "USD1",
    "rate": 1.0,
    "timestamp": "2023-10-01T12:00:00Z"
}

def insert_dummy_payload():
    # Connect to MongoDB
    client = MongoClient(MONGO_URI)
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]
    
    # Insert the dummy payload into the collection
    result = collection.insert_one(dummy_payload)
    print(f'Inserted document ID: {result.inserted_id}')

if __name__ == "__main__":
    insert_dummy_payload()