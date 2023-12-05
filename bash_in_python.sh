import os

# Define variables
command_1 = 'whoami'
command_2 = 'ip a'
command_3 = 'lshw -short'

# Execute bash commands using os.system()
os.system(command_1)
os.system(command_2)
os.system(command_3)

# Print messages
print("Bash commands executed successfully using Python and the os module.")
print("The result of the 'whoami' command:")
print("-------------------------------")
print()

# You could use subprocess module for capturing command output
# Below is an example of how subprocess.run() can be used to capture output.
# This requires using subprocess module, not os
import subprocess

output = subprocess.run(command_1.split(), capture_output=True, text=True)
print(output.stdout)

# Similarly, you can capture and print output of other commands
# For instance, command_2 and command_3 using subprocess.run()
