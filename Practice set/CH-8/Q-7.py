# Write a recursive function to print numbers from 1 to n

def print_numbers(n):
    if n == 0:
        return
    print_numbers(n - 1)  # Recursive call to print smaller numbers first
    print(n)  # Print the current number

# Example usage:
print_numbers(5)
