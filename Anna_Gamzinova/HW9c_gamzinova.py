# Finding all the numbers from 1-1000 that are divisible by 7

divided_by_7 = [number for number in range(1, 1000) if number % 7 == 0]
print(divided_by_7)

# second solution using a generator comprehension
# for item in (number for number in range(1, 1000) if number % 7 == 0):
#     print(item)
