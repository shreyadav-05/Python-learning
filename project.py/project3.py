# number guess game


import random

play = "yes"

while play.lower() == "yes":
   
    
    level = input("Choose difficulty (easy/medium/hard): ").lower()
    
    if level == "easy":
        secret = random.randint(1, 10)
        max_attempts = 5
    elif level == "medium":
        secret = random.randint(1, 50)
        max_attempts = 7
    elif level == "hard":
        secret = random.randint(1, 100)
        max_attempts = 10
    else:
        print("Invalid choice, defaulting to easy level.")
        secret = random.randint(1, 10)
        max_attempts = 5

    attempts = 0
    guessed = False
    
    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess == secret:
            print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
            guessed = True
            break
        elif guess < secret:
            print("📈 Too low!")
        else:
            print("📉 Too high!")
    
    if not guessed:
        print(f"❌ Sorry, you couldn't guess the number. It was {secret}.")
    
    play = input("Do you want to play again? (yes/no): ")




