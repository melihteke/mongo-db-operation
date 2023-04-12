from pymongo import MongoClient
from bson.objectid import ObjectId
import environment


DB_URI = environment.DB_URI
DB_NAME = environment.DB_NAME
DB_COLLECTION_NAME = environment.DB_NAME

class MongoDBOperation:
    def __init__(self, uri, db_name, collection_name):
        self.client = MongoClient(uri)
        self.db = self.client.get_database(db_name)
        self.collection = self.db.get_collection(collection_name)

    def add_record(self, record):
        self.collection.insert_one(record)

    def remove_record(self, record_id):
        self.collection.delete_one({'_id': ObjectId(record_id)})

    def update_record(self, record_id, updates):
        self.collection.update_one({'_id': ObjectId(record_id)}, {'$set': updates})

    def view_all_records(self):
        return [record for record in self.collection.find()]

    def view_specific_record(self, filters):
        return [record for record in self.collection.find(filters)]
