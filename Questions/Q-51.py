#check Perfect Number
num = 28
divisors = [i for i in range(1, num) if num % i == 0]
if sum(divisors) == num:
    print(num, "is a Perfect Number")
else:
    print(num, "is not a Perfect Number")
