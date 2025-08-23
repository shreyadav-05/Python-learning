#Count Vowels in a String
text = input("Enter a word or sentence: ").lower()
vowels = "aeiou"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Number of vowels:", count)
