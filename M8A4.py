# Name: Axel Mendez
# Student ID: 882349616
# Section: CPSC 223P-07
# Assignment: Module 8 Assignment 4

file_name = input("What is the file with the data? ")
def dictionary_maker(path):
    try:
        ret_dict = {}
        with open(path) as file_object:
            data = file_object.read()
            data_list = data.split('\n')
            for object in data_list:
                key, value = object.split(':')
                ret_dict[key] = value
    except FileNotFoundError:
        print(f"The file {path} does not exist on this system")
    print(ret_dict)

dictionary_maker(file_name)
