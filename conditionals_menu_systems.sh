#!/bin/bash

# Script Name:                  conditionals_menu_systems.sh
# Author Name:                  Israel QuirolaSalas
# Date of latest revision:      11/30/2023
# purpose:                      
# Execution:                    bash conditionals_menu_systems.sh or ./conditionals_menu_systems.sh chmod -x aconditionals_menu_systems.sh
# Additional Sources:

# Declaration of variables


# Declarations of functions

# Main

while true
do
    echo "Menu:"
    echo "1. Hello world"
    echo "2. Ping self"
    echo "3. IP info"
    echo "4. Exit"
    read -p "Enter your choice: " choice

    case $choice in
        1)
            echo "Hello world!"
            ;;
        2)
            ping -c 4 127.0.0.1
            ;;
        3)
            ip a
            ;;
        4)
            echo "Exiting..."
            exit 0
            ;;
        *)
            echo "Invalid option. Please choose again."
            ;;
    esac
done

# End