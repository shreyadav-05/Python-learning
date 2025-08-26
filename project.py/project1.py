#Rock paper , scissor.

import random
'''
-1 Rock
1  Parer
0  scissor
'''

computer = random.choice([-1,1,0])
youDict = {"R":-1 , "P":1 , "S":0}
reverseDict = {-1:"Rock 🪨" , 1:"Paper 📰" , 0:"Scissor ✂️"}

youstr = input("enter your choice:")
print(" ")
you = youDict[youstr]
print(f" You chose: {reverseDict[you]}\n Computer chose: {reverseDict[computer]} ")

print(" ")
if(computer == you):
    print("it's a Draw 🟰")
else:
 if(computer == -1 and you == 1):
    print("you Win 🎉")
 elif(computer == -1 and you == 0):
    print("you Loss ☠️")
 elif(computer == 1 and you == -1):
    print("you Loss ☠️")
 elif(computer == 1 and you == 0):
    print("you Win🎉")
 elif(computer == 0 and you == -1):
    print("you Win🎉")
 elif(computer == 0 and you == 1):
    print("you Loss ☠️")
 else:
    print("something went wrong ")










"""Features to be added soonn!!

    1. add play again option
   2. Add a score board 
   3. Shortne the if_else statements

"""