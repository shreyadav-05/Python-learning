# #A spam comment is defined as a text containing following keywords:
# "Make a lot of money", "buy now", "subscribe this", "click this". write a program to detect these spam messages 


# spam filter system
s1= "Make a lot of money"
s2= "make a lot of money"

s3= "Buy now"
s4 = "buy now"

s5 = "Subscribe this"
s6 = "subscribe this"

s7= "click this"
s8= " Click this"

message=input("Comment here: ")

if((s1 and s2 in message) or (s4 and s3 in message ) or (s5 and s6 in message) or (s7 or s8 in message)):
  print("it's a spam comment")

else:
  print("it is not valid comment ")


