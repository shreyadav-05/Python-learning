#Check if two strings are anagrams
s1, s2 = "listen", "silHent"
if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")
