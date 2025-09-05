# vowel counter check
string = input("enter the string:")
vowels = ["a","e","i","o","u"]

count = 0
for ch in string:
    if ch in vowels :
        count +=1
print ("Total vowels :",count)



# #find the maximum element in a list 
numbers = [55,23,90,58,68]
max_num = numbers [0]
for num in numbers:
    if num > max_num:
        max_num = num
        print("maximum element:",max_num)

#Check prime number
num = int(input("enter the num"))
if num > 1:
    for i in range(2,num):
        if num % i == 0:
            print(num, "is not prime number")
            break
        else:
            print(num," is a prime number")
            
