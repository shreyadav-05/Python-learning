# write a recursive function to find the sum of digits of a number.

def sum_of_digits(n):
    # Convert to positive in case n is negative
    n = abs(n)
    
    # Base case: single digit
    if n < 10:
        return n
    
    # Recursive case
    return (n % 10) + sum_of_digits(n // 10)

# Example usage:
number = 467587698
print(f"Sum of digits of {number} is {sum_of_digits(number)}")
