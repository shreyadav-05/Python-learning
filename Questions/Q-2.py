# Write a program to print the multiplication table of a number using a for loop


num = int(input("Enter a number: "))
print(f"\nMultiplication Table of {num}")
for i in range(1, 11):   
    print(f"{num} x {i} = {num * i}")
