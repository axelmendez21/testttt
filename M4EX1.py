# Name: Axel Mendez
# Student ID: 882349616
# Section: CPSC 223P-07
# Assignment: Module 4 Assignment EX1

cities_list = []
nyc_dict = {
    "name": "New York City",
    "pop": 8580000,
    "sate": "New York",
    "teams": ["Yankees", "Mets", "Knicks", "Nets", "Liberty", "NY Giants", "Jets"]
}
la_dict = {
    "name": "Los Angeles",
    "pop": 3870000,
    "sate": "California",
    "teams": ["Rams", "Chargers", "Lakers", "Clippers", "Sparks", "Dodgers", "Angels", "Kings", "Ducks"]
}
chic_dict = {
    "name": "Chicago",
    "pop": 2750000,
    "sate": "Illinois",
    "teams": ["Bears", "Cubs", "White Sox", "Bulls", "BlackHawks", "Sky", "Fire FC", "Red Stars", "Hounds"]
}

cities_list.append(nyc_dict)
cities_list.append(la_dict)
cities_list.append(chic_dict)

favteam = input("what is your favorite team? ")
for city in cities_list:
    if favteam in city.get("teams"):
        print(f"If you like the {favteam} you should move to {city.get("name")}")