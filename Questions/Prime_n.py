# 


num = int(input("enter a num: "))
if num == 1:
    print("1 not a prime Number nor Composite") 
elif num ==2:
  print("2 is a prime number")
elif num>1:
    for i in range (2 , num):    
     if num % i ==0:  
        print(num , "is not a prime num")
        break
    
    else:
        print(num, "is a prime num")


