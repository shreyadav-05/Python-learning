#Append text to an existing file
with open("myfile.txt", "a") as f:
    f.write("Adding another line to the file.\n")
print("Text appended successfully.")
