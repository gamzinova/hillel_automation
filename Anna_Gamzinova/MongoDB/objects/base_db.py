import pymongo
from bson import ObjectId


class BaseDB:
    def __init__(self, database, collection):
        self.connection = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
        self.database = self.connection[database]
        self.collection = self.database[collection]

    def insert_values(self, my_tuples: tuple):
        """
        list should be filled with dicts, with such format {'name': new_name, 'color': new_color, 'occupation':
        new_occupation}
        """
        return self.collection.insert_many(
            [{'name': insert_i[0], 'color': insert_i[1], 'occupation': insert_i[2]} for insert_i in my_tuples])

    def find_value(self, filter_db=None):
        return self.collection.find_one(filter=filter_db)

    def find_all_values(self):
        return [x for x in self.collection.find()]

    def delete_item_by_id(self, del_id: str):
        if not isinstance(del_id, ObjectId):
            del_id = ObjectId(del_id)
        return self.collection.delete_one({'_id': del_id})

    def delete_all_objects(self):
        return self.collection.delete_many({})
