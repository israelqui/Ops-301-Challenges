#!/usr/bin/env python3

# Script: Python File Handling
# Author: Israel Quirola
# Date: Dec 8, 2023

# Create a new text file
file_name = 'example.txt'

with open(file_name, 'w') as file:
    # Append three lines to the file
    file.write("This is line 1\n")
    file.write("This is line 2\n")
    file.write("This is line 3\n")

# Read and print the first line
with open(file_name, 'r') as file:
    first_line = file.readline()
    print("First line of the file:", first_line)

# Delete the file
import os
if os.path.exists(file_name):
    os.remove(file_name)
    print(f"{file_name} deleted successfully")
else:
    print(f"{file_name} does not exist")
    
