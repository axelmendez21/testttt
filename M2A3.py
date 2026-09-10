# Name: Axel Mendez
# Student ID: 882349616
# Section: CPSC 223P-07
# Assignment: Module 2 Assignment 3

uber_list = list(range(100,202,2))
choice1 = int(input("What is the start of your slice? "))
choice2 = int(input("What is the end of your slice? "))
data_list = uber_list[choice1 : choice2]
total_int = 0
for data in data_list:
    total_int += data
total_int = total_int / len(data_list)
print(f"Your slice contains {len(data_list)} values and has an average value of {total_int}")