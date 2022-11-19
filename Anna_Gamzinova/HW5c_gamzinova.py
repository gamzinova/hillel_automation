# Converting string into dictionary

info = "name=Amanda=sssss&age=32&&salary=1500&currency=euro"

# First split by delimiter: &
split_info = info.split("&")
temp_list = []
dict_info = dict()

# Creating dictionary from the split result
for split_i in split_info:
    temp_list = split_i.split("=")
    # if the list has at least 2 values update dict info, ignore other values
    if len(temp_list) > 1:
        dict_info.update({temp_list[0]: temp_list[1]})
print(dict_info)

