class StarbucksMug:
    def __init__(self, collection: str, city: str, colour: str, price: float):
        if collection:
            self.__collection = collection
        else:
            raise ValueError("The collection field can not be empty")

        if city:
            self.__city = city
        else:
            raise ValueError("The city field can not be empty")
        if colour:
            self.__colour = colour
        else:
            raise ValueError("The colour field can not be empty")
        if (type(price) == int or type(price) == float) and price > 0:
            self.__price = price
        else:
            raise ValueError("The price should be a number higher than 0")

    @property
    def collection(self):
        return self.__collection.title()

    @collection.setter
    def collection(self, new_collection):
        if new_collection:
            self.__collection = new_collection
        else:
            print("The value collection can not be empty")

    @property
    def city(self):
        return self.__city.capitalize()

    @city.setter
    def city(self, new_city):
        if new_city:
            self.__city = new_city
        else:
            print("The value city can not be empty")

    @property
    def colour(self):
        return self.__colour.capitalize()

    @colour.setter
    def colour(self, new_colour):
        if new_colour:
            self.__colour = new_colour
        else:
            print("The value colour can not be empty")

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("The new price should be higher than 0")

    def __str__(self):
        mug = f"{self.__class__.__name__}:{{\n" \
              f"\tcollection: {self.collection}\n" \
              f"\tcity: {self.city}\n" \
              f"\tcolour: {self.colour}\n" \
              f"\tprice: {self.price} $\n}}"
        return mug


if __name__ == '__main__':
    my_mug = StarbucksMug("you are here", "copenhagen", "yellow", 15)
    print(my_mug)
