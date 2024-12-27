import os

def list_directory_contents(directory):
    try:
        # Get the list of all files and directories in the specified directory
        contents = os.listdir(directory)
        print(f"Contents of '{directory}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"Error: The directory '{directory}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to access '{directory}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Specify the directory you want to list
# Here u can enter ur path directory
directory_path = "/Iqoo Neo 6"
list_directory_contents(directory_path)


'''# Another Approach of this question

import os

# Select the directory whose content you want to list
directory_path = '/'

# Use os module to list the directory content
contents = os.listdir(directory_path)

# print content of the directory
print(contents)'''
