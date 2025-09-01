#Find all prime numbers in a range
start, end = 10, 30
for n in range(start, end+1):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            print(n, end=" ")
