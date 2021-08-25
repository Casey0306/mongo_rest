import pymongo
from bson.objectid import ObjectId


class MongoDB:

    def __init__(self, username, password, ip, dbname):
        self.username = username
        self.password = password
        self.ip = ip
        self.dbname = dbname

    def __connect(self):
        client = None
        try:
            uri = "mongodb://" + self.username + ":" + \
                  self.password + "@" + \
                  self.ip + "/" + self.dbname
            client = pymongo.MongoClient(uri)
        except Exception as e:
            print(str(e))
        return client

    def create_item(self, collection_name, params):
        client = self.__connect()
        db = client[self.dbname]
        collection = db[collection_name]
        collection.insert_one(params)
        client.close()

    def find_item(self, collection_name, params):
        client = self.__connect()
        db = client[self.dbname]
        collection = db[collection_name]
        documents = collection.find(params)
        result = []
        result_document = {}
        for document in documents:
            result_document["id"] = str(document["_id"])
            if "name" in document:
                result_document["name"] = document["name"]
            result.append(result_document)
            result_document = {}
        client.close()
        return result

    def find_item_detail(self, collection_name, param_id):
        client = self.__connect()
        db = client[self.dbname]
        collection = db[collection_name]
        item_id = ObjectId(param_id)
        document = collection.find_one({"_id": item_id})
        temp_id = str(document["_id"])
        del document["_id"]
        document["id"] = temp_id
        result = document
        client.close()
        return result
