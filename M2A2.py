# Name: Axel Mendez
# Student ID: 882349616
# Section: CPSC 223P-07
# Assignment: Module 2 Assignment 2

g_list = ['Mortal Kombat', 'Contra', 'Streets Of Rage', 'Shinobi', 'Sonic', 'Phantasy Star']

print("Here are the top Sega games:")
for game in g_list:
    print(game.title())
remove = input("Which one do you think should be removed? ")
g_list.remove(remove)
print("Here are the new top Sega games:")
for game in g_list:
    print(game.title())