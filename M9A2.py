# Name: Axel Mendez
# Student ID: 882349616
# Section: CPSC 223P-07
# Assignment: Module 9 Assignment 2

starting_string = """Print this in uppercase
Print this in lowercase
Print this as a title
Print this left justified (80 characters, with ='s)
Print this right justified (80 characters, with +'s)"""

lines_of_text = starting_string.split('\n')
print(f"{lines_of_text[0].upper()}")
print(f"{lines_of_text[1].lower()}")
print(f"{lines_of_text[2].title()}")
print(f"{lines_of_text[3].ljust(80, '=')}")
print(f"{lines_of_text[4].rjust(80, '+')}")
print(f"{';'.join(lines_of_text)}")
first = starting_string.find('j')
second = starting_string.find('j', first+1)
print(starting_string[second:second+5])


