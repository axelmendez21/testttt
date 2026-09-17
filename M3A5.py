# Name: Axel Mendez
# Student ID: 882349616
# Section: CPSC 223P-07
# Assignment: Module 3 Assignment 5

start_int = int(input("What is the first number? "))
end_int = int(input("What is the second number? "))
num_list = list(range(start_int,end_int+1))
sum_int = 0

for num in num_list:
    if num%5 == 0:
        sum_int += num
print(f"The total value of multiples of {start_int} to {end_int} is {sum_int}")