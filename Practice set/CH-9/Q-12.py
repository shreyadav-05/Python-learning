#Write a program to mine a log file and find out whether it contains python.
with open("log.txt")as f:
    content = f.read()

if("pokemon" in content):
    print("yes Pokemon is present")
else:
    print("no Pokemon is not present")
