#Write a program to find out whether a file is identical & matches the content of another file.
with open("file.txt") as f:
    content1 = f.read()   # use content1 instead of contant

with open("poem.txt") as f:
    content2 = f.read()

if content1 == content2:
    print("Yes, these files are identical")
else:
    print("No, these files are not identical")
