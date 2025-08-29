#Replace "Donkey" with "######"
# Problem 4
with open("file.txt", "r") as f:
    content = f.read()

content = content.replace("Donkey", "######")

with open("file.txt", "w") as f:
    f.write(content)
