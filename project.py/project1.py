
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

user_score = 0
computer_score = 0
while True:
    computer = random.choice([-1, 1, 0])
    youstr = input("\nEnter your choice (R/P/S): ").upper()

    if youstr not in youDict:
        print("❌ Invalid input! Please choose R, P, or S.")
        continue

      
      
    you = youDict[youstr]
    print(f" You chose: {reverseDict[you]}\n Computer chose: {reverseDict[computer]} ")

   
    if(computer == you):
        print("it's a Draw 🟰")

    elif(you == -1 and computer == 0) or (you == 1 and computer == -1) or (you == 0 and computer == 1):
        print("🎉 You Win!")
        user_score += 1
    else:
        print("☠️ You Lose!")
        computer_score += 1

    #      Display current scores
    print(f"\n🏆 Scoreboard:")
    print(f"You: {user_score} | Computer: {computer_score}")

    #       Play again option 
    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("\n👋 Thanks for playing!")
        print(f"Final Scores → You: {user_score} | Computer: {computer_score}")
        break
   

"""
import random

# Mapping dictionaries
youDict = {"R": -1, "P": 1, "S": 0}
reverseDict = {-1: "Rock 🪨", 1: "Paper 📰", 0: "Scissor ✂️"}

# Scoreboard initialization
user_score = 0
computer_score = 0

print("🎮 Welcome to Rock-Paper-Scissors Game 🎮")
print("Use: R for Rock, P for Paper, S for Scissors")

while True:
    computer = random.choice([-1, 1, 0])
    youstr = input("\nEnter your choice (R/P/S): ").upper()

    if youstr not in youDict:
        print("❌ Invalid input! Please choose R, P, or S.")
        continue

    you = youDict[youstr]

    print(f"\nYou chose: {reverseDict[you]}")
    print(f"Computer chose: {reverseDict[computer]}")

    # Determine the result
    if computer == you:
        print("🟰 It's a Draw!")
    elif (you == -1 and computer == 0) or (you == 1 and computer == -1) or (you == 0 and computer == 1):
        print("🎉 You Win!")
        user_score += 1
    else:
        print("☠️ You Lose!")
        computer_score += 1

    # Display current scores
    print(f"\n🏆 Scoreboard:")
    print(f"You: {user_score} | Computer: {computer_score}")

    # Play again option
    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("\n👋 Thanks for playing!")
        print(f"Final Scores → You: {user_score} | Computer: {computer_score}")
        break
"""















"""Features to be added soonn!!

    1. add play again option
   2. Add a score board 
   3. Shortne the if_else statements

"""