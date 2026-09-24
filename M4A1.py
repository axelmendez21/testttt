# Name: Axel Mendez
# Student ID: 882349616
# Section: CPSC 223P-07
# Assignment: Module 4 Assignment 1

g_list = []
g_list.append(input("What is your number 1 favorite Playstation game? "))
g_list.append(input("What is your number 2 favorite Playstation game? "))
g_list.append(input("What is your number 3 favorite Playstation game? "))

for num, game in enumerate(g_list, start=1):
    print(f"Your number {num} favorite game was {game}")