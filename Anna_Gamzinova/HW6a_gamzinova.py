# creating a list of tuples and save to file

from random import randint
import os

list_tuples = list()
# a is left number, b is right number and c is operator
for index in range(0, 100, 1):
    a = randint(0, 100)
    b = randint(0, 100)
    c = randint(1, 3)
    list_tuples.append((a, b, c))
# print(list_tuples)

os.makedirs("test/data")
path = './test/data'
file = "list_tuples.txt"
with open(os.path.join(path, file), 'w') as fp:
    for tuple_line in list_tuples:
        fp.write(f'{tuple_line[0]} {tuple_line[1]} {tuple_line[2]}\n')

