#!/usr/bin/env python3

# Script: Directory Creations
# Author: Israel Quirola
# Date:

# Import libraries

import os

# Declaration of variables

user_path = input("Enter directory path: ")

### Read user input here into a variable

# Declaration of functions
def generate_directory_structure(directory_path):
    for (root, dirs, files) in os.walk(directory_path):
        
        print(root)
        
        print(dirs)
        
        print(files)


# Main
### Pass the variable into the function here

generate_directory_structure(user_path)

# End