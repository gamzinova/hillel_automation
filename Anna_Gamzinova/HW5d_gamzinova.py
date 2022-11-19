# Converting camel case to snake
import re

camel_list = ["FirstItem", "FriendsList", "MyTuple"]
snake_list = []

# for each word in camel list find matching regex and replace with _ and change to lower case
for camel_word in camel_list:
    snake_list.append(re.sub('([a-z])([A-Z])', r'\1_\2', camel_word).lower())

print(snake_list)
