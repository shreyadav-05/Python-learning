#Print multiplication tables from 1 to 5
for num in range(1, 8):
    print("\nTable of", num)
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)
