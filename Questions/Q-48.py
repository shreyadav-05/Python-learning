#Check Anagram (Two Strings)
str1 = "listen"
str2 = "silent"

if sorted(str1) == sorted(str2):
    print(str1, "and", str2, "are Anagrams")
else:
    print(str1, "and", str2, "are not Anagrams")
