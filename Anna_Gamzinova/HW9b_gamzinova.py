def my_generator():
    """
    A function that returns the squares of even elements
    """
    counter = 0
    while counter <= 1000000000:
        if counter % 2 == 0:
            yield pow(counter, 2)
        counter += 1


for even_number in my_generator():
    print(even_number)

