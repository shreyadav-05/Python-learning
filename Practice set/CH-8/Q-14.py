# Factorial (Recursive)

def factorial(n):
    if n == 0 or n == 1:  # base case
        return 1
    return n * factorial(n-1)

print(factorial(5))  # Output: 120
