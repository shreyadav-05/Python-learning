#Write a program that asks for two numbers and prints which one is larger.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(a, "is larger")
elif b > a:
    print(b, "is larger")
else:
    print("Both are equal")
