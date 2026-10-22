# Name: Axel Mendez
# Student ID: 882349616
# Section: CPSC 223P-07
# Assignment: Module 7 Assignment 2


class User:
    def __init__(self, first_name, last_name,user_id,last_login,password):
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.last_login = last_login
        self.password = password
    def describe_user(self):
        print(f"Accessing user {self.user_id}:")
        print(f"{self.first_name} {self.last_name} last logged in on {self.last_login}")
    def greet_user(self):
        print(f"Welcome to the jungle {self.first_name} {self.last_name}, you gonna die")
    
    def new_login(self, month, day, year):
        months = {
            1: 'January',
            2: 'Febuary',
            3: 'March',
            4: 'April',
            5: 'May',
            6: 'June',
            7: 'July',
            8: 'August',
            9: 'September',
            10: 'October',
            11: 'November',
            12: 'December'
        }
        if (int(day) < 1 or int(day) > 31):
            print("That is not a valid day")
        elif (int(month) < 1 or int(month) > 12):
            print("That is not a valid month")
        elif (int(year) < 1):
            print("that is not a valid year")
        else:
            self.last_login = f'{months[month]} {day}, {year}'
            
        
class Admin(User):
    def __init__(self, first_name, last_name,user_id,last_login,password):
        super().__init__(first_name, last_name,user_id,last_login,password)
        self.privileges = []
    def show_privileges(self):
        print(f"{self.first_name} {self.last_name} has the following privileges:")
        for privilege in self.privileges:
            print(f"{privilege}")
    def add_privilege(self, privilege):
        self.privileges.append(privilege)

# hard-coded calls
jim = User(first_name='Jim',
           last_name='Bob',
           user_id=1000,
           last_login='June 12, 1998',
           password='password123')
jim.describe_user()
jim.greet_user()
joe = User('Joe',
           'Bob',
           1001,
           'July 4, 2001',
           'babygirl')
joe.greet_user()
joe.describe_user()
joe.new_login(2, 3, 2025)
joe.describe_user()
joe.new_login(15, 3, 2025)
joe.new_login(2, 35, 2025)
joe.new_login(2, 3, -55)

alice = Admin('Alice',
              'Wonder',
              1,
              'September 3, 2022',
              'P@ssw0rd')
alice.add_privilege('delete post')
alice.add_privilege('delete user')
alice.add_privilege('add user')
alice.add_privilege('give admin rights')
alice.show_privileges()