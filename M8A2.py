# Name: Axel Mendez
# Student ID: 882349616
# Section: CPSC 223P-07
# Assignment: Module 8 Assignment 2

with open("input.txt") as file_object:
    data = file_object.read()

data_list = data.split('\n')

with open("output.txt",'a') as file_object:
    for line in data_list:
        print(line, file = file_object)