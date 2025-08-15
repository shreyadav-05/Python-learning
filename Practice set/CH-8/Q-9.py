# Write a recursive function to reverse a string


def reverse_string(s):
    # Base case: if the string is empty or has one character, return it
    if len(s) <= 1:
        return s
    # Recursive case: reverse the rest of the string and add the first character at the end
    return reverse_string(s[1:]) + s[0]

# Example usage:
text = "Shreya"
print(reverse_string(text))  # Output: "olleh"
