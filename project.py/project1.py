#Rock paper , scissor.

'''
-1 Rock
1  Parer
0  scissor
'''
computer = -1
youstr = input("enter your choice:")
youDict = {"R":-1 , "P":1 , "S":0}
reverseDict = {-1:"Rock" , 1:"Paper" , 0:"Scissor"}
you = youDict[youstr]
print("you chose{reverseDict[you]}\n computer chose{reverseDict[computer]}")
if(computer == you):
    print("its a draw")
else:
 if(computer == -1 and you == 1):
    print("you win")
 elif(computer == -1 and you == 0):
    print("you loss")
 elif(computer == 1 and you == -1):
    print("you loss")
 elif(computer == 1 and you == 0):
    print("you win")
 elif(computer == 0 and you == -1):
    print("you win")
 elif(computer == 0 and you == 1):
    print("you loss")
 else:
    print("something went wrong ")