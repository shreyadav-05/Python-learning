#Add a static method in problem 2, to greet the user with hello.import math

class Calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        return self.number ** 2

    def cube(self):
        return self.number ** 3

    def square_root(self):
        return math.sqrt(self.number)

    @staticmethod
    def greet():
        print("Hello! Welcome to the Calculator class.")


Calculator.greet()
num = Calculator(16)
print("Square:", num.square())
print("Cube:", num.cube())
print("Square Root:", num.square_root())
