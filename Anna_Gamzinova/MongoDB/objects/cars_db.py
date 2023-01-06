from Anna_Gamzinova.MongoDB.objects.base_db import BaseDB


class Cars(BaseDB):
    def __init__(self):
        super().__init__("cars", "cars_characters")

    def insert_value(self, new_name, new_color, new_occupation):
        """
        dict format is {'name': new_name, 'color': new_color, 'occupation': new_occupation}
        """
        return self.collection.insert_one({'name': new_name, 'color': new_color, 'occupation': new_occupation})
