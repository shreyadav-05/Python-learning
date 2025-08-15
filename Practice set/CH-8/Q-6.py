# Write a recursive function to print numbers from n to 1

def countdown(n):
    if n <= 0:  # Base case
        return
    print(n)
    countdown(n - 1)  # Recursive call

# Example usage:
countdown(5)
