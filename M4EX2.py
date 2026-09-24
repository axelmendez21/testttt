# Name: Axel Mendez
# Student ID: 882349616
# Section: CPSC 223P-07
# Assignment: Module 4 Assignment EX2

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

count = {}

for person, food in food_dict.items():
    count[food] = 0
for person, food in food_dict.items():
    count[food] += 1

highestfood = ""
highestnum = 0
for food, counted in count.items():
    if highestnum == 0:
        highestnum = counted
        highestfood = food
    elif counted > highestnum:
        highestnum = counted
        highestfood = food

print(f"The most popular food is {highestfood}")