# Calculate sum of all numbers from 1 to a given number
def sum(n):
  i=1
  s=0
  a=0
  while(i<n+1):
    s=s+i
    i+=1
    a=s/n
  return s,a


n=int(input("enter: "))
s,a=sum(n)
print(f"Sum is {s}")
print(f"Average is {a}")
