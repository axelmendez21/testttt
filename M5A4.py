# Name: Axel Mendez
# Student ID: 882349616
# Section: CPSC 223P-07
# Assignment: Module 5 Assignment 4

orders_list = ['pastrami', 'turkey', 'pastrami', 'ham', 'turkey']
finished_list = []
while orders_list:
    finish = orders_list.pop()
    print(f"I made your {finish}")
    finished_list.append(finish)
print("Here are all the sandwiches I made:")
for finished in finished_list:
    print(finished)