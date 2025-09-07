# Add a static method in problem 2, to greet the user with hello 
"""Q-4"""
class calculator:
  def __init__(self,n):
    self.n=n

  def square(self):
    print(f"The square is {self.n*self.n}")
  def cube(self):
    print(f"The cube is {self.n*self.n*self.n}")
  def sqaureroot(self):
    print(f"The square root is {self.n**1/2}")
  @staticmethod
  def greet():
    print("Hello, good morning😊 ")

a=calculator(4)
a.greet()
a.square()
a.sqaureroot()
a.cube()

