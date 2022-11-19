# List of odd and even numbers

# number_list = [1, 2, 3, 4, 5, 6, 7, 8]
number_list = list(range(1, 9))

odd = list()
even = list()

for index, number, in enumerate(number_list):
    # print(f'index is {index}, value is {number}')
    if number % 2 == 0:
        even.append((index, number))
    else:
        odd.append((index, number))
print(even)
print(odd)

