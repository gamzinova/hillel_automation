from Anna_Gamzinova.MongoDB.objects.base_db import BaseDB


class Cars(BaseDB):
    def __init__(self):
        super().__init__("cars", "cars_characters")
