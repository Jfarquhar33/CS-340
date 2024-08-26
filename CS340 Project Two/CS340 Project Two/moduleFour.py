from pymongo import MongoClient
from bson.objectid import ObjectId


    
class AnimalShelter:
    """ CRUD operations for Animal collection in MongoDB """
    
    def __init__(self, username, password):
    	
        connection_uri = f'mongodb://{username}:{password}@nv-desktop-services.apporto.com:31886/AAC'

        self.client = MongoClient(connection_uri)

        self.database = self.client['AAC']
        self.collection = self.database['animals']
        
    # Implementing method for C of CRUD	
    def create(self, data):
        if data is not None:
            result = self.database.animals.insert(data)
            if result != 0:
            	return True
            else:
            	return False   
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
	# Implenting method for R of CRUD
    def read(self, criteria=None):  
        if criteria:
            cursor = self.collection.find(criteria, {"_id": 0})
        else:
            cursor = self.collection.find({}, {"_id": 0})
        for document in cursor:
            yield document
   
   # Implementing method for U in CRUD
    def update(self, initial, change):
        if initial is not None:
            if self.database.animals.count_documents(initial, limit = 1) != 0:
                update_result = self.database.animals.update_many(initial, {"$set": change})
                result = update_result.raw_result
            else:
                result = "No document found"
            return result
        else:
            raise Exception("Nothing to update, data parameter is empty")

   # Implementing method for D in CRUD
    def delete(self, remove):
        if remove is not None:
            if self.database.animals.count_documents(remove, limit = 1) != 0:
                delete_result = self.database.animals.delete_many(remove)
                result = delete_result.raw_result
            else:
                result = "No document found"
            return result
        else:
            raise Exception("Nothing to delete, data parameter is empty")
