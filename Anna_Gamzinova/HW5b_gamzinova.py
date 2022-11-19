# Names in the column centered

names = ["John", "Marta", "James", "Amanda", "Marianna"]
title = "Names"

# Printing the results
print(f"{title.center(20, '*')}")

for name in names:
    print(f"{name:>20}")

