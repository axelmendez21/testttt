# Name: Axel Mendez
# Student ID: 882349616
# Section: CPSC 223P-07
# Assignment: Module 7 Assignment 2

class NumCouple:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def minimum(self):
        if (int(self.num1) < int(self.num2)):
            return int(self.num1)
        return int(self.num2)
    def maximum(self):
            if (int(self.num1) > int(self.num2)):
                return int(self.num1)
            return int(self.num2)
    def product(self):
         return int(self.num1 * self.num2)

class NumThruple(NumCouple):
    def __init__(self, num1, num2, num3):
          super().__init__(num1,num2)
          self.num3 = num3
    def minimum(self):
        if (super().minimum() < self.num3):
             return super().minimum()
        else:
            return self.num3
    def maximum(self):
            if (super().maximum() > self.num3):
                 return super().maximum()
            return self.num3
    def product(self):
         return (super().product() * self.num3)

# hard-coded lines
couple = NumCouple(4, 7)
print(f"The couples minimum is {couple.minimum()}")
print(f"The couples maximum is {couple.maximum()}")
print(f"The couples product is {couple.product()}")
thruple = NumThruple(3, 5, 2)
print(f"The thruples minimum is {thruple.minimum()}")
print(f"The thruples maximum is {thruple.maximum()}")
print(f"The thruples product is {thruple.product()}")