#Repeat program 4 for a list of such words to be censored.


word = ["Shreya","Pooja","Anusatha"]
with open("file.txt","r")as f:
    content = f.read()
for word in word:
    content = content.replace(word,"#" * len(word))
    with open("file.txt","w")as f:
        f.write(content)
