#  Fibonacci Number

def fibonacci(n):
    if n <= 1:  # base case
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))  # Output: 8
