#NEWLY ADDED FEATURES IN PYTHON
#Following are some of the newly added features in Python programming language.

#WALRUS OPERATOR
# The walrus operator (:=), introduced in Python 3.8, allows you to assign values to variables as 
# part of an expression. This operator is named for its resemblance to the eyes and tusks of a walrus,
#  officially called the assignment expression.



"""
# using walrus operator
if (n := len([1, 2, 3, 4, 5])) > 4:
    print(f"List is too long ({n} elements, expected <= 4)")
#In this example, n is assigned the value of len([1, 2, 3, 4, 5]) and then used in the comparison within the if statement.


#TYPES DEFINITIONS IN PYTHON
#Type hints are used for indicating the content signature for variables and function return types.
# Variable type hint
age: int = 25
# Function type hints
def greeting(name: str) -> str:
    return f"Hello, {name}!"
# Usage
print(greeting("Shreya"))    # Output: Hello, Alice!


#ADVANCED TYPE HINTS
#Python's typing module provides more advanced type hints, such as List, Tuple, Dict, and Union.
#You can import List, Tuple and Dict types from the typing module like this:

from typing import List, Tuple, Dict, Union



#The syntax of types looks something like this:
from typing import List, Tuple, Dict, Union

# List of integers
numbers: List[int] = [1, 2, 3, 4, 5]

# Tuple of a string and an integer
person: Tuple[str, int] = ("Alice", 30)

# Dictionary with string keys and integer values
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}

# Union type for variables that can hold multiple types
identifier: Union[int, str] = "ID12345"   # also valid: 12345
#These annotations help in making the code self-documenting and allow developers to understand 
# the data structures used at a glance.

#MATCH CASE
#Python 3.10 introduced the match statement, which is similar to the switch statement
#found in other programming languages.
#The basic syntax of the match statement involves matching a variable against several
#cases using the case keyword.


def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status"
        
print(http_status(5007))  # Output: Unknown Status
print(http_status(200))   # Output: OK
print(http_status(404))   # Output: Not Found
print(http_status(500))   # Output: Internal Server Error
print(http_status(400))   # Output: Unknown Status

#DICTIONARY MERGE & UPDATE OPERATORS
#New operators | and |= allow for merging and updating dictionaries.
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Merge dictionaries
dict3 = dict1 | dict2
print(dict3)     # Output: {'a': 1, 'b': 3, 'c': 4}

# Update dictionary
dict1 |= dict2
print(dict1)     # Output: {'a': 1, 'b': 3, 'c': 4}


#you can also now use multiple context managers in a single with statement more cleanly
#using the parenthesized context manager:
#with (
#    open("file1.txt") as f1,
#    open("file2.txt") as f2
#):
#    #process files
#    pass

#EXCEPTION HANDLING IN PYTHON
#(Left side wali faint line: “Exception handling is used in Python when something goes wrong.”)
#(Doosri faint line: “Exception in Python can be handled explicitly in the code that handles the
#exception written in the except clause.”)

try:
    a = int(input("Hey, Enter a number: "))
    print(a)

except ValueError as v:
    print("Heyyyy")
    print(v)

except Exception as e:
    print(e)

print("Thank you")
"""

"""
try:
    # Code
except ZeroDivisionError:
    # Code
except TypeError:
    # Code
except:
    # All other exceptions are handled here.
"""

"""
#RAISING EXCEPTIONS
#We can raise custom exceptions using the raise keyword in Python.

a = int(input("Enter a number :"))
b = int(input("Enter second number:"))

if(b == 0):
    raise ZeroDivisionError("Hey our program is not meant to divice number by zero")

else:
    print(f"The division a/b is {a/b}")


#TRY WITH ELSE CLAUSE
#Sometimes we want to run a block of code only when no exception was raised.
try:
    a = int(input("Hey, Enter a number: "))
    print(a)

except Exception as e:
    print(e)

else:
    print("I am inside else")


#TRY WITH FINALLY
#Python offers a ‘finally’ clause which ensures execution of a piece of code irrespective of the exception.
try:
    a = int(input("Hey, Enter a number: "))
    print(a)

except Exception as e:
    print(e)

finally:
    print("I am inside of finally")


#finally use
def main():   
    try:
        a = int(input("Hey, Enter a number: "))
        print(a)
        return
    
    except Exception as e:
        print(e)
        return
    
    finally:
        print("I am inside of finally")

main()

#if __name__ == "__main__": in Python##

#__name__ evaluates to the name of the module in Python from where the program is run.
#If the module is being run directly from the command line, the __name__ is set to the 
# string "__main__". Thus, this behaviour is used to check whether the module is run directly 
# or imported to another file.
"""
def myFunc():
    print("Hello world!")
if __name__ == "__main__": 
    #if this code is directly executed by running the file its present in
    print("We are directly running this code")


myFunc()
print(__name__)

#THE GLOBAL KEYWORD
#The global keyword is used to modify the variable outside of the current scope.
a = 89
def fun():
    #global
    a = 3
    print(a)

fun()
print(a)

#THE GLOBAL KEYWORD
#The global keyword is used to modify the variable outside of the current scope.
l = [3, 513, 53, 535]

index = 0
for item in l:
    print(f"The item number at index {index} is {item}")
    index += 1
