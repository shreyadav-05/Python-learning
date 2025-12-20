#write a list comprehension to print a list which contains the multiplication table of a user enterd number.
n = int(input("enter a nuber"))

table = [n*i for i in range(1,11)]
print(table)

