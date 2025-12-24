#  Virtual Environment (venv)

#A virtual environment is an isolated Python environment that allows each project to have its own dependencies and
#package versions without affecting other projects.

#installation
#Create virtual environment using python -m venv env_name
#Activate using env_name\Scripts\activate
#Install required packages
#Deactivate after use



#environment activate
#(myenv\Scripts\activate)

#Terminal me:
#((myenv)

#Command
#(pip freeze)
#pip freeze command
#pip freeze is a command used to display all installed Python packages along with their versions in the current environment.


#requirements.txt
#pip freeze > requirements.txt

#pip install -r requirements.txt #Dusre system me same packages install karne ke liye

#Lambda function
#A lambda function is a small anonymous function defined using the lambda keyword that can take any number of arguments but only one expression.


#normal function vs lamda function
#normal
def add(a, b):
    return a + b

#lamda
add = lambda a, b: a + b
#Syntax
lambda arguments : expression
#lambda → keyword
#arguments → input
#expression → calculation / logic
#return likhne ki zarurat nahi hoti



#EX-
#Square of a number
square = lambda x: x * x
print(square(5))

#Add two numbers
add = lambda a, b: a + b
print(add(10, 20))

#Even or Odd check
check = lambda n: "Even" if n % 2 == 0 else "Odd"
print(check(7))


#Lambda with built-in functions
#map()#Har element pe function apply karta hai
nums = [1, 2, 3, 4]
result = list(map(lambda x: x * 2, nums))
print(result)

#filter()#Condition true hone wale elements leta hai
nums = [1, 2, 3, 4, 5]
result = list(filter(lambda x: x % 2 == 0, nums))
print(result)

#reduce() (from functools)Sab values ko combine karta hai
from functools import reduce

nums = [1, 2, 3, 4]
result = reduce(lambda a, b: a + b, nums)
print(result)



#join() method
#The join() method is used to combine elements of an iterable into a single string using a specified separator.
#Syntax
#separator.join(iterable) separator → jo beech me aayega  and  iterable → list / tuple / set (strings ka)
#EX-
words = ["Hello", "World"]
result = " ".join(words)
print(result)


#Different Separators ke examples
#Comma se join
names = ["Ram", "Shyam", "Mohan"]
print(",".join(names))


#Hyphen se join
print("-".join(names))

#Empty string (no space)
print("".join(names))
