#Read file line by line with line numbers
# Program 5
with open("myfile.txt", "r") as f:
    for i, line in enumerate(f, 1):
        print(f"Line {i}: {line.strip()}")
