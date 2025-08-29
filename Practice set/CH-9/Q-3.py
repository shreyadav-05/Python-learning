#Count number of words in a file
# Program 3
with open("myfile.txt", "r") as f:
    content = f.read()

words = content.split()
print("Number of words:", len(words))

