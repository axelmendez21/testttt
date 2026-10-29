import os.path

filename = "junk.txt"

try:
    with open(filename) as file_object:
        text = file_object.read()
except FileNotFoundError:
    print(f"Sorry, but {filename} does not exist")
else: 
    print(text)