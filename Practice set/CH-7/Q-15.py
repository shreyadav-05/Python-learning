# write a program to calculate  the factorial of a given number using for loop 

"""Q-15"""
n = (int(input("enter: ")))
fac=1
for i in range(1, n+1):
 fac *= i 
print(f"The factorial of {n} is {fac}") 
