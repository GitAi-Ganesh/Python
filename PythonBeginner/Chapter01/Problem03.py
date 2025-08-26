# Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that. 
import os

# Specify the directory you want to list
directory = "/"

# List all files and subdirectories
try:
    contents = os.listdir(directory)
    print(f"Contents of directory '{directory}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"The directory '{directory}' does not exist.")
except PermissionError:
    print(f"Permission denied to access '{directory}'.")
