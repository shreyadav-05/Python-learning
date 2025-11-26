# Write a fucntions to calculate and return the square of a number

def square(num):
    result = num * num      # multiply number by itself
    return result           # return the answer

# taking input from user
number = int(input("Enter a number: "))

# calling the function
ans = square(number)

# printing the result
print("Square of", number, "is:", ans)

