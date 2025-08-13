#                                       LOOPs            
# Sometime we want to repeat a set of statement in our program. for instance: print 1 to 1000

# LOOPS make it easy for programmer to tell the computer which set od instructions to repeat and how !!

# Types of LOOPS in python
"""
1. While loops
2. For loops
""" 

#1. WHILE LOOP --> In while loop condition is checked first then, if it evaluates to true it will execute otherwise not !!
i=0
while(i<6):     # we provide the condition(i<6), This block keeps executing until the condition is true 
  print(i)         #[  body of    ]
  i+=1             #[    loop     ]


# * if the condition never becomes false then it is said to be the infinte loop
'''
OUTPUT:
0
1
2
3
4
5

'''

# while loop using list 
l=[1,"harry","subham", "divya","aditya", "anmol", "annirudh", False ]

i=0

while(i<len(l)):
  print(l[i])
  i+=1

'''
OUTPUT:
1
harry
subha
divya
adity
anmol
annirudh
False
'''  

#2. FOR LOOP -->> A loop is used to iterate through sequence like list, tuple, or string[iterables]
#when you know how many times repeat
#EX-
for i in range(8):
   print("hello")
   # This will print "hello" 5 times 


l=[1,7,5]
for a in l:      # Here, 'a' is a temporary loop variable which stores each element and then displays it."
  print(a)      # print the item --> 1,7 and 5

# loop-iterate-

l = [1,2,4,6,56,467,4,786]
for i in l:
   print(i)

# tuple-
t = [6,576,65,6,687]
for i in t:
   print(i)

# string
S = "Shreya"
for i in S:
   print(i)



# Loop through a string
for char in "cat":
    print(char)  
'''   
OUTPUT:
c
a
t 
'''
# LOOP through string only printing the first 4 letters of my Name
string="SHREYA YADAV"
for i in string[:4]:    # it is done by the string slicing method 
   print(i)
'''
OUTPUT:
S
H
R
E
Y
A
'''
# Loop through a dictionary
d = {"a": 1, "b": 2}
for key in d:
    print(key, d[key])  
    
'''   
OUTPUT:
a 1
b 2
'''
# This makes for loops flexible — they work with many data types by iterating over their elements in order.


#RANGE funciton in python
'''
The range() fucntion in python is used to gerante a sequence of number.

range() specify the start, stop and step-size

'''
for i in range(0,20,5):  #t will generate a sequence starting from 0 up to (but not including, n-1) 20, with a step size of 5.
  print(i) 
'''  
OUTPUT:
0
5
10
15
'''

# LOOP through string only printing the first 4 letters of my Name
string="SHREYA YADAV"
for i in range(4):
   print(string[i])

'''
OUTPUT:
S
H
R
E
Y
A
'''

# for-with-else.py-

l = [1,7,8]
for item in l:
   print(item)
else:
   print("done") 

   # break
   for i in range (100):
      if (i == 34):
         break #exit the loop right now
   print(i)
    

# continue
for i in range(100):
   if (i == 34):
      continue # skip this iteration
   print(i)
      
   