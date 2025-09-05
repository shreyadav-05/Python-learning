num = int(input("enter num:"))
if num == 1:
    print("1 is not a prime number nor composite")
elif num == 2:
    print("2 is prime number")
    
elif num > 1:
    for i in range(2 , num):
        if num % i == 0:
            print(num, "is not prime number")
            break
        else:
            print(num," is a prime number")
            