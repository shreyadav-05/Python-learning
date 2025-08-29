#Find "python" in a log file
# Problem 6
with open("log.txt", "r") as f:
    content = f.read()

if "python" in content.lower():
    print("Yes, 'python' is present in the log file.")
else:
    print("No, 'python' is not present in the log file.")
