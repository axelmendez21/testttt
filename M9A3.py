# Name: Axel Mendez
# Student ID: 882349616
# Section: CPSC 223P-07
# Assignment: Module 9 Assignment 3

def print_board(list):
    
    top = "-" * (len(list)*2+1)
    print(top)
    for pattern in list:
        print("|" + "|".join(pattern) + "|")
        print(top)

board1_list = [['*','*','*'],
               ['*','+','*'],
               ['*','*','*']]
print_board(board1_list)
print() #just for a spacer line
board2_list = [['*',' ',' ','*'],
               ['*',' ',' ','*'],
               ['*',' ',' ','*'],
               ['*',' ',' ','*']]
print_board(board2_list)
print() #just for a spacer line
board3_list = [['*',' ','*',' ','*'],
               [' ','*',' ','*',' '],
               [' ',' ',' ',' ',' '],
               [' ','+',' ','+',' '],
               ['+',' ','+',' ','+']]
print_board(board3_list)