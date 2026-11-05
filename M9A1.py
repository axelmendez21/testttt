# Name: Axel Mendez
# Student ID: 882349616
# Section: CPSC 223P-07
# Assignment: Module 9 Assignment 1

population_dict = {}
small = ""
while True:
    city = input("What is the next city? (enter q to quit) ")
    if (city == 'q'):
        small = input("What is the largest population for a small town? ")
        break
    pop = input(f"What is the population of {city}? ")
    population_dict[city] = pop

with open("populationdata.txt",'w') as file_object:
    print("Big Cities:", file = file_object)
    for city, population in population_dict.items():
        if int(population) > int(small):
            print(f"{city}, {population}", file = file_object)
    print("Small Towns:", file = file_object)
    for city, population in population_dict.items():
        if int(population) <= int(small):
            print(f"{city}, {population}",file = file_object)
    