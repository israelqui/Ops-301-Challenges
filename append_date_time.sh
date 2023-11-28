#!/bin/bash

# Script Name:                  append_date_time.sh
# Author Name:                  Israel QuirolaSalas
# Date of latest revision:      11/28/2023
# purpose:                      automating log generation
# Execution:                    bash add.sh or ./add.sh chmod -x add.sh
# Additional Sources:           https://chat.openai.com/

# Declaration of variables


current_date=$(date +"%Y %B %d %A %H %M %S")
## This line uses the date command with a specific format (+%Y%m%d_%H%M%S) to obtain the current date and time in the format YYYYMMDD_HHMMSS. This result is stored in the variable current_date.

echo $current_date
## This outputs the actual date and time in the terminal 

destination_file="syslog_${current_date}.log"
## Here, the variable destination_file is defined. It takes the string "syslog_" and appends the value stored in current_date, creating a filename that incorporates the date and time obtained from the earlier command. Finally, ".log" is added as the file extension.
cp /var/log/syslog "./$destination_file" &> log_copy_output.txt
## The cp command then copies /var/log/syslog to the current directory using the filename specified in destination_file.

echo "Copied /var/log/syslog to ./$destination_file at $(date)" >> log_actions.txt
##echo: This command in Bash is used to print/display text or variables on the terminal. "Copied /var/log/syslog to ./$destination_file at $(date)": This is the text that will be echoed. It's a message indicating that the file /var/log/syslog has been copied to the current directory with the name stored in the variable $destination_file, and it includes the current date and time. $(date) is a command substitution that inserts the current date and time into the string when executed. >> log_actions.txt: This part of the command redirects the output of the echo command and appends it to a file named log_actions.txt. The >> operator is used for appending. If the file doesn't exist, it will be created; if it exists, the output will be added to the end of the file without overwriting existing content. Therefore, when this line executes, it appends the specified message, including the information about the copied file and the timestamp, to the log_actions.txt file.
# Declarations of functions

# Main