#Store the multiplication tables generated in problem 3 in file named Tables.txt.
n = int(input("enter a numbr"))
table = [n*i for i in range(1, 11)]
with open("table.txt","a") as f:
    f.write(f"Table of {n}:{str(table)}\n")