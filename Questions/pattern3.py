#  Write a program to print the following star pattern
"""
for n=3
***
* *  
***

"""
"""Q-9"""
n= int(input("enter:"))

for i in range(1, n+1):
  print("*"*(n))
  print("*",end="")
  print(" "* (n-2),end="")          #I did it,
  print("*" )                   # but not in the correct way
  print("*" * n)
  break


""" Correct way to do"""
n= int(input("enter: " ))

for i in range(1, n+1):
  if(i==1 or i==n):
    print("*" * n, end="")
  else:
    print("*",end="")
    print(" " *(n-2), end="")
    print("*", end="")
  print("")
