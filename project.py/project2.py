# simple calculator🧮



a = int(input("enter the number a:"))
b = int(input("enter the number b:"))
op = input ("🧠 enter operation (+, -, *, /, %, ^)")
  
if op == "+":
    print("➕result:" , a+b)

elif op == "-":
    print("➖result:" , a-b)

elif op == "*":
    print("✖result:" , a*b)

elif op == "%":
    print("💯result:" , a*b) / 100

elif op == "^":
    print("⚡result:" , a**b)   

elif op == "/":
  if b == 0:
      print("➗result:" , a/b)

  else:
    print("cannot divide by zero")
else:
    print("❌invalid operation , please enter (+, -, *, /, %, ^)")






    



