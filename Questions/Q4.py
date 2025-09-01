#Check if a number is Armstrong number
#(Armstrong number = sum of its digits raised to power of number of digits)
n = 153
digits = str(n)
power = len(digits)
if sum(int(d)**power for d in digits) == n:
    print("Armstrong Number")
else:
    print("Not Armstrong")
