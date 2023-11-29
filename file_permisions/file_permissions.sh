#!/bin/bash

# Script Name:                  file_permissions.sh
# Author Name:                  Israel QuirolaSalas
# Date of latest revision:      11/29/2023
# purpose:                      
# Execution:                    bash file_permissions.sh or ./file_permissions.sh chmod -x file_permissions.sh
# Additional Sources:

# Declaration of variables


# Declarations of functions

# Main


# Prompt user for input directory path
echo "Enter the directory path:"
read directory
# These lines prompt the user to enter a directory path and store the input in the variable directory using the read command.

# Check if the directory exists
if [ ! -d "$directory" ]; then
    echo "Directory not found!"
    exit 1
fi
# This block of code checks if the directory entered by the user exists (-d checks if it's a directory). If the directory doesn't exist, it prints an error message and exits the script with a status code of 1.

# Prompt user for input permissions number
echo "Enter the permissions number (e.g. 777):"
read permissions
# Similar to the first input, these lines prompt the user to enter a permissions number (e.g., 777) and store it in the variable permissions.


# Change permissions of files in the directory
chmod -R "$permissions" "$directory"
# This line uses the chmod command to recursively (-R) change the permissions of the directory and its contents to the permissions specified by the user.


# Print directory contents
echo "Directory contents:"
ls -l "$directory"
# This line prints the contents of the directory (ls -l lists in long format) after the permissions change.


# Print new permissions settings
echo "New permissions settings:"
stat -c "%A %n" "$directory"/*
# This line uses the stat command to display the new permissions settings for all files and subdirectories in the specified directory. %A displays the permissions in a human-readable format, and %n displays the file/directory name.

# End