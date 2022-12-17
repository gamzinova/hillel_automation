import pymongo


class BaseDB:
    def __init__(self, database, collection):
        self.connection = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
        self.database = self.connection[database]
        self.collection = self.database[collection]

    def insert_value(self, new_name, new_color, new_occupation):
        """
        dict format is {'name': new_name, 'color': new_color, 'occupation': new_occupation}
        """
        return self.collection.insert_one({'name': new_name, 'color': new_color, 'occupation': new_occupation})

    def insert_values(self, my_tuples: tuple):
        """
        list should be filled with dicts, with such format {'name': new_name, 'color': new_color, 'occupation':
        new_occupation}
        """
        return self.collection.insert_many(
            [{'name': insert_i[0], 'color': insert_i[1], 'occupation': insert_i[2]} for insert_i in my_tuples])

    def find_value(self):
        return self.collection.find_one()

    def find_all_values(self):
        return [x for x in self.collection.find()]

    def delete_item_by_name(self, del_name: str):
        return self.collection.delete_one({'name': del_name})

    def delete_all_objects(self):
        return self.collection.delete_many({})
