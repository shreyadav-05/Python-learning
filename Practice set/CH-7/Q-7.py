#count and print how many numbers between 1 to 50 are divisible by 7.

count = 0
for i in range (1 , 51):
    if i % 7 == 0:
        print(i)
        count=count+1
        print("total:" , count )