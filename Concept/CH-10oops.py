#What is OOP (Object Oriented Programming)?
"""
OOP is a style of programming where we divide our code into classes and objects.
Class = Design / Blueprint (like a house plan)
Object = The real thing created from that design (like the actual house built from the plan)
"""

#🔹 Why do we use OOP?
"""
Organize code – Makes big programs easier to understand and maintain.
Reuse code – We can reuse classes multiple times.
Solve real-world problems – Helps model real-world entities like Car, Student, or BankAccount.
"""


#🔹 How to use OOP in Python?
#Example 1: Simple Class & Object
# Creating a Class
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def study(self):
        print(f"{self.name} is studying.")

# Creating an Object
s1 = Student("Rahul", 20)
s1.study()   # Output: Rahul is studying.

#Example 2: Inheritance (Parent → Child)
class Animal:
    def sound(self):
        print("Makes some sound.")

class Dog(Animal):
    def sound(self):
        print("Dog barks - Woof Woof!")

d = Dog()
d.sound()   # Output: Dog barks - Woof Woof!

#🔹 4 Pillars of OOP (in Simple English)
"""
Encapsulation → Grouping data and functions together inside a class.
Inheritance → Using features of one class in another.
Polymorphism → Same name, different behavior (e.g., same method → different results).
Abstraction → Show only important details, hide unnecessary ones.
"""


#👉 In simple words:
#OOP is a style of coding where we write programs as if we are working with real-life objects.



#🏦 Real-Life Example: Bank Account System
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. Current Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. Current Balance: {self.balance}")
        else:
            print("Insufficient Balance!")

    def check_balance(self):
        print(f"Account Holder: {self.account_holder}, Balance: {self.balance}")


# Creating an account
acc1 = BankAccount("Rahul", 1000)

acc1.check_balance()
acc1.deposit(500)
acc1.withdraw(300)
acc1.withdraw(2000)

#🖥 Output:
"""
Account Holder: Rahul, Balance: 1000
500 deposited. Current Balance: 1500
300 withdrawn. Current Balance: 1200
Insufficient Balance 
"""


#🔑 What did we learn?
"""
Class → BankAccount is the blueprint.
Object → acc1 is Rahul’s account.
Encapsulation → Balance + methods are grouped inside one class 
Real-life use → Works like a real bank account.
"""
 