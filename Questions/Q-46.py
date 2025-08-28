#Check Armstrong Number
num = 6678
s = sum(int(d)**3 for d in str(num))
if num == s:
    print(num, "is an Armstrong Number")
else:
    print(num, "is not an Armstrong Number")
