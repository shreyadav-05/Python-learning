# Write a recursive function to find the sum of numbers from 1 to n




def sum_recursive(n):
    # Base case
    if n <= 1:
        return n
    # Recursive case
    return n + sum_recursive(n - 1)

# Example usage:
print(sum_recursive(5))  # Output: 15
