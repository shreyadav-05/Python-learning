#Create a class with a class attribute a; create an object from it and set'a' directly using object.a=o. Does this change the class attribute?
class demo:
  a= 4

o =demo()
print(o.a)   # prints the class attribute because no instance attribute set there
o.a = 0    # instance attribute set
print(o.a)  # prints the instance attribute

print(demo.a) # no class attribute doesn't change 
# prints the class attribute because no instance attribute set there


"""Object Oriented Programming
Class → Blueprint of an object"""
