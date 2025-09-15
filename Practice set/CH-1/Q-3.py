#  write a python program to print the content of a directory using the OS module. search online for the function which does that.
 

import os

# Specify the directory path (you can change this)
path = "/"

# List all files and directories in the given path
try:
    contents = os.listdir(path)
    print(f"Contents of directory '{path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"The directory '{path}' does not exist.")
except PermissionError:
    print(f"No permission to access '{path}'.")





    

