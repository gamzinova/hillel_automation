# reading the file and performing mathematical operations on each element

import os

path = './test/data'
file = "list_tuples.txt"

# open list of tuples file
with open(os.path.join(path, file), 'r') as fp:
    list_lines = fp.read().splitlines()

# calculate mathematical operations using list
for line in list_lines:
    # a is left number, b is right number and c is operator
    line_split = line.split(" ")
    a = int(line_split[0])
    b = int(line_split[1])
    c = int(line_split[2])

    if c == 1:
        print(f'{a} + {b} = {a + b}')
    elif c == 2:
        print(f'{a} - {b} = {a - b}')
    elif c == 3:
        print(f'{a} * {b} = {a * b}')

