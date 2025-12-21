#WAP to display a/b where a and b are integers .If b = 0, display infinite by handlind the 'ZeroDivisionError'.
try:
    a = int(input("enter a: "))
    b = int(input("enter b: "))
    print(a/b)
except ZeroDivisionError as v:
    print("infinite")