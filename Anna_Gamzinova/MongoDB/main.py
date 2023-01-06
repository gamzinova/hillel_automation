from Anna_Gamzinova.MongoDB.objects.cars_db import Cars

cars = Cars()
cars.insert_values(
    (["Lightning McQueen", "red", "Race Car"],
     ["Don Hudson", "blue", "Judge"],
     ["Mater", "brown", "Tow Truck"]))
print(f'1.\t{cars.find_value()}')
print(f'2.\t{cars.find_all_values()}')
new_character = cars.insert_value("Sally", "light blue", "Lawyer")
print(f'3.\t{cars.find_all_values()}')
print(cars.find_value(filter_db={"name": "Lightning McQueen"}).get("_id"))
found_car_id = cars.find_value(filter_db={"name": "Lightning McQueen"}).get("_id")
cars.delete_item_by_id(found_car_id)
print(f'4.\t{cars.find_all_values()}')
print(f'5.\t{cars.find_value(filter_db={"name": "Don Hudson"})}')
cars.delete_all_objects()
print(f'6.\t{cars.find_all_values()}')
