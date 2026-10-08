# Name: Axel Mendez
# Student ID: 882349616
# Section: CPSC 223P-07
# Assignment: Module 6 Assignment 4

def show_messages(messages_list):
    while messages_list:
        print(f"{messages_list.pop()}")
my_messages = []

while True:
    message = input("What is the next message? (type 'q' to quit) ")
    if message == 'q':
        print("First time calling function")
        show_messages(my_messages[:])
        print("Second time calling function")
        show_messages(my_messages[:])
        break
    my_messages.append(message)
    

