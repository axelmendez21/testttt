# Name: Axel Mendez
# Student ID: 882349616
# Section: CPSC 223P-07
# Assignment: Module 4 Assignment 3

games_dict = {}

for i in range(3):
    greatgame = input("What is a great game? ")
    games_dict[greatgame] = input ("What system can I play that on? ")

print("That's too many, let's get rid of one")
remove = input("What game should we remove? ")
games_dict.pop(remove)
print("The new dictionary is:")

for game, system in games_dict.items():
    print(f"You can play {game} on {system}")