#Conditionals are used to make decisions in a program. They check whether a condition is true or false, and then execute different blocks of code based on the result.
#"If something is true, do this.Otherwise, do something else."

# Basic Conditional Statement: if
age = 18

if age >= 18:
    print("You are an adult.")

# If the condition age >= 18 is True, it prints "You are an adult."



# With else (if condition is False)
age = 16

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

#With elif (else if – check multiple conditions)
marks = 85

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
else:
    print("Grade: C")


   #EXAMPLE
age = 20

if age >= 18:
    print("You can vote.")
else:
    print("You are too young to vote.")
    
     #If your age is 18 or more, it prints: "You can vote."If your age is less than 18, it prints: "You are too young to vote."


# Keywords to remember:
#if -  check a condition
#elif-  check another condition (optional)
#else - do this if nothing else matched










