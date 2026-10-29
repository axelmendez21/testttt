# Name: Axel Mendez
# Student ID: 882349616
# Section: CPSC 223P-07
# Assignment: Module 8 Assignment 1

with open("input.txt") as file_object:
    data = file_object.read()

data_list = data.split('\n')
for line in data_list:
    print(line)