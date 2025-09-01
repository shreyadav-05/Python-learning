
# Write a python program to read the content of a file "poem.txt" and check if the word is present in the file or not.
f = open("poem.txt")
content = f.read()
if("step" in content):
    print("the word step is present in the content")
else:
    print("the word step isz present in the content")
    f.close()