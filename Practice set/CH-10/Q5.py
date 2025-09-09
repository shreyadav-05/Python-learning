#Create a class with a class attribute a; create an object from it and set a directly using object.a = 0. Does this change the class attribute?
class Sample:
    a = 10   # class attribute

obj = Sample()
print("Initially:", obj.a)   # 10



obj.a = 0    # creates instance attribute, does NOT change class attribute
print("After changing obj.a:", obj.a)
print("Class attribute still:", Sample.a)
