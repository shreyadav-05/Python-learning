#Write a class “Calculator” capable of finding square, cube and square root of a number.
class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square is {self.n * self.n}")

a = Calculator(7)
a.square()

