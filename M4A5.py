# Name: Axel Mendez
# Student ID: 882349616
# Section: CPSC 223P-07
# Assignment: Module 4 Assignment 5

food_dict = {'Jim': 'Tacos',
             'Bob': 'Burgers',
             'Janelle': '',
             'Lisa': 'Pizza',
             'Thomas': '',
             'Yolanda': '',
             'Finn': 'Bread',
}

for person, food in food_dict.items():
    if food == '':
        food_dict[person] = input(f"What is {person}'s favorite food? ")

print("Here are the favorite foods: ")
for person, food in food_dict.items():
    print(f"{person}'s favorite food is {food}")