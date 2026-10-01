# Name: Axel Mendez
# Student ID: 882349616
# Section: CPSC 223P-07
# Assignment: Module 5 Assignment 2

start = input("Enter the start of the loop: ")
limit = input("Enter the limit of the loop: ")
current = int(start)
while current < int(limit):
    print(f"The current value is {current}")
    current = current * 2
print(f"The last value of current that was less than {limit} was {str(current//2)}")