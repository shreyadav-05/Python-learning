# vowel counter check
string = input("enter the string:")
vowels = ["a","e","i","o","u"]

count = 0
for ch in string:
    if ch in vowels :
        count +=1
print ("Total vowels :",count)
