# Name: Axel Mendez
# Student ID: 882349616
# Section: CPSC 223P-07
# Assignment: Module 5 Assignment 3

print("Welcome to the trivia builder 3000")
triviabank_dict = {}

keep_going = True
while keep_going:
    question_str = input("Enter the next question: ")
    if question_str == 'Done':
        break
    if question_str == '':
        print("You did not enter a question, let's try again.")
        continue
    answer_str = input("Enter the correct answer for that question: ")
    triviabank_dict[question_str] = answer_str
print("We will stop entering questions now")
print("Here is the final trivia dictionary:")
for question, answer in triviabank_dict.items():
    print(f"The question is: {question}")
    print(f"And the answer is: {answer}")
