# Name: Axel Mendez
# Student ID: 882349616
# Section: CPSC 223P-07
# Assignment: Module 3 Assignment 6

student_name = input("What is the student name? ")
student_score = int(input("What is their score? "))

if student_score >= 90 and student_score <= 100:
    print(f"{student_name} earned an A")
elif student_score >=80 and student_score < 90:
    print(f"{student_name} earned an B")
elif student_score >=70 and student_score < 80:
    print(f"{student_name} earned an C")
elif student_score >=60 and student_score < 70:
    print(f"{student_name} earned an D")
elif student_score < 60:
    print(f"{student_name} earned an F")