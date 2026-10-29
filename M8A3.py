# Name: Axel Mendez
# Student ID: 882349616
# Section: CPSC 223P-07
# Assignment: Module 8 Assignment 3

first_num = input("What is the first number? (or type q to quit) ")
while first_num != 'q':
    second_num = input("What is the second number? ")
    try:
        answer = int(first_num) / int(second_num)
        print(f"{first_num} / {second_num} is {answer}")
    except ZeroDivisionError:
        print("You cannot divide by 0")
    first_num = input("What is the first number? (or type q to quit) ")
print("The program is over")