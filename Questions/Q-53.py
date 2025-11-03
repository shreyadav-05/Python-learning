#
num = int(input("Enter a number: "))
rev = int(str(num)[::-1])

if num == rev:
    print("Palindrome number")
else:
    print("Not a palindrome number")
