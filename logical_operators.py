#!/usr/bin/env python3

# Script: Logical Operations
# Author: Israel Quirola
# Date: dec 7, 2023

# This part of the script defines a Python class called Car. Classes in Python serve as blueprints to create objects with specific properties and behaviors. In this case, the Car class has attributes such as make, model, year, and mileage, which are initialized through the __init__ method

class Car:
    def __init__(self, make, model, year, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage


# Creating two car objects
car1 = Car("Toyota", "Corolla", 2018, 30000)
car2 = Car("Honda", "Civic", 2020, 25000)

print()

# Comparing car attributes using logical conditionals
if car1.make == car2.make:
    print("Both cars are the same make")
else:
    print("The cars are different makes")

print()

# 'f' for example replaces car1.make for the actual make and model of the car 
if car1.year < car2.year:
    print(f"{car1.make} {car1.model} is an older model than {car2.make} {car2.model}")
else:
    print(f"{car1.make} {car1.model} is a newer model than {car2.make} {car2.model}")

print()

if car1.mileage != car2.mileage:
    print(f"The mileage of {car1.make} {car1.model} is different from {car2.make} {car2.model}")
else:
    print(f"The mileage of {car1.make} {car1.model} is the same as {car2.make} {car2.model}")

print()

if car1.year >= car2.year:
    print(f"{car1.make} {car1.model} is as new as or newer than {car2.make} {car2.model}")
else:
    print(f"{car1.make} {car1.model} is older than {car2.make} {car2.model}")

print()

if car1.mileage > car2.mileage:
    print(f"{car1.make} {car1.model} has higher mileage than {car2.make} {car2.model}")
else:
    print(f"{car1.make} {car1.model} has lower or equal mileage than {car2.make} {car2.model}")

print()

# Comparing car attributes using logical conditionals with if, elif, and else

if car1.make == car2.make:
    print("Both cars are of the same make")
elif car1.year < car2.year:
    print(f"{car1.make} {car1.model} is an older model than {car2.make} {car2.model}")
else:
    print("Neither the make nor year conditions are met for these cars")
print()