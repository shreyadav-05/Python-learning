#Count frequency of each character in a string
s = "programming"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)
