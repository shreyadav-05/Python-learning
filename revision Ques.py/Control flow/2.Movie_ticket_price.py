# Movie ticket are priced based on age $12 for adults
# (18 and over), $8 for children, Everyone gets a $ 2 discount on 
# wednesday 

age = int(input("enter your age:"))
day = input("enter day")
if age >= 18:
    price = 12
else:
    price = 8
if day == "wednesday":
    price-= 2
print(f"your ticket price {price}")

