#!/usr/bin/env python3

# challenges

print() # line break

# assign a variable to a list of strings.

cars = ["Ford", "Chevrolet", "Dodge", "Toyota", "Subaru", "Nissan", "Mercedez", "BMW", "VW", "Audi"]

# each element has an index representing its position. Lists in Python are zero-indexed, meaning the first element has an index of 0, the second element has an index of 1, and so on.
# 'print(cars)'

for index, cars in enumerate(cars):
    print(f"{index + 1}: {cars}")

print() # line break

# print the fourth element of the list.

cars = ["Ford", "Chevrolet", "Dodge", "Toyota", "Subaru", "Nissan", "Mercedez", "BMW", "VW", "Audi"]
print(cars[3])

print() # line break

# Print the six element through tenth element of the list.

cars = ["Ford", "Chevrolet", "Dodge", "Toyota", "Subaru", "Nissan", "Mercedez", "BMW", "VW", "Audi"]
print(cars[5:10])

print() # line break

# Change the value of the seventh element to "onion"

cars = ["Ford", "Chevrolet", "Dodge", "Toyota", "Subaru", "Nissan", "Mercedez", "BMW", "VW", "Audi"]
cars[6] = "onion"
print(cars)

print()

# append
cars = ["Ford", "Chevrolet", "Dodge", "Toyota", "Subaru", "Nissan", "Mercedez", "BMW", "VW", "Audi"]
cars.append("Volvo")
print(cars)
