# mujhe nhi a raha yeh m chatgpt se punch rhii

print("Prime num from 1 to n " )
num = int(input("enter n:"))
for i in range (2 , num):               
        if (num % i)  == 0:      
           print(f"{num} is not prime")     
           break
        else:
         print(f"{num} is  a prime number")
        break