# vowel counter check
"""

string = input("enter the string:")
vowels = ["a","e","i","o","u"]

count = 0
for ch in string:
    if ch in vowels :
        count +=1
print ("Total vowels :",count)
"""


# #find the maximum element in a list 
"""
numbers = [55,23,90,58,68]
max_num = numbers [0]
for num in numbers:
    if num > max_num:
        max_num = num
        print("maximum element:",max_num)
"""
#Check prime number
"""
num = int(input("enter the num"))
if num > 1:
    for i in range(2,num):
        if num % i == 0:
            print(num, "is not prime number")
            break
        else:
            print(num," is a prime number")
"""

# Right-angled triangle pattern
"""
*
**
***
****
*****

rows = 5
for i in range (1,rows+1):
    print("*" * i)
"""    







# Reverse a string 
# Take a string as input and print it in reverse using a for loop.
# ulta string prine karwana hai example = Shreya 
#             output = ayerhs
"""
text = input("enter the string:")
reversed_text = text[:: -1]
print("reversed string:",reversed_text)
"""







# Fibonacci sequence
# Print the first n terms of the Fibonacci sequence using a for loop.
# 👉 (e.g., 0, 1, 1, 2, 3, 5, 8...)

"""

n = int(input("enter the number:"))
a , b = 0 , 1
print("fibonacci series:")
for i in range(n):
    print(a,end = "")
    a, b = b ,a+b

"""










# Armstrong number check
# Check if a number is an Armstrong number (e.g., 153 = 1³ + 5³ + 3³).
# Use a loop to calculate powers.










# Number pyramid pattern
# Print this pattern for n = 5:
"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5



rows = 5
for i in range(1, rows+1):
    for j in range(1,i+1):
        print(j , end="")
    print()
"""

# print half pyramid
"""

rows = 5
for i in range( rows):
    for j in range (i+1):
        print("*",end = " ")
    print()
"""
    


#reverse 
"""
rows = 5
for i in range(rows, 0 ,-1):
    for j in range (i):
        print("*",end = " ")
    print()
"""


#fibonaci sedries
"""
n = int(input("enter the number:"))
a , b = 0 , 1
print("fibonacci series:")
for i in range(n):
    print(a,end = "")
    a, b = b ,a+b

"""