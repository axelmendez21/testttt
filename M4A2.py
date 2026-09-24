# Name: Axel Mendez
# Student ID: 882349616
# Section: CPSC 223P-07
# Assignment: Module 4 Assignment 2

food_dict = {}

for i in range(3):
    chosenfood = input("What is good to eat? ")
    food_dict[chosenfood] = input ("What country is that from? ")

food = input("What dish do you like? ")
print(f"{food} is from {food_dict[food]}")