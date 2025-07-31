# lable the program written in problem 4 with comments.

import os

# Select the directory whose content you want to list 
path = "/"

try:

    #use the OS module to list the directory content
    contents = os.listdir(path)
    print(f"Contents of directory '{path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"The directory '{path}' does not exist.")
except PermissionError:
    print(f"No permission to access '{path}'.")
    
