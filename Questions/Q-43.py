#Fibonacci Series (First 10 Numbers)
a, b = 0, 1
print("Fibonacci series:", end=" ")
for _ in range(10):
    print(a, end=" ")
    a, b = b, a+b
