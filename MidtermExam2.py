# Name: Axel Mendez
# Student ID: 882349616
# Section: CPSC 223P-07
# Assignment: Midterm Exam 2

firstnum_int = int(input("Enter a first number: "))
secondnum_int = int(input("Enter a second number: "))

if firstnum_int > secondnum_int:
    print("The first number is greater than the second number")
elif secondnum_int > firstnum_int:
    print("The first number is less than the second number")
else:
    if (firstnum_int%2) == 0:
        print("The first number is equal to the second number and they are both even")
    else:
        print("The first number is equal to the second number and they are both odd")