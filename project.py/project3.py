# number guess game


import random #Yeh Python ko bolta hai ki “main random numbers banana chahti hoon”.Jaise tum “lucky number” ke liye kisi se random number bulwati ho, waise hi program bhi ek random number choose karega.

play = "yes" #Yeh ek variable hai jo batata hai ki game chalana hai ya band karna hai.Starting me "yes" rakha gaya hai taaki game start ho jaaye.

while play.lower() == "yes":   #Yeh ek loop hai jo tab tak chalega jab tak user "yes" likhega.Agar user "no" likhega,to loop ruk jaayega aur game khatam.lower() ka matlab hai — agar user “YES”, “Yes”, “yEs” likhe bhi, to bhi sab "yes" me convert ho jaata hai.
   
    
    level = input("Choose difficulty (easy/medium/hard): ").lower()  #Yeh user se difficulty level poochta hai.User likhega — “easy”, “medium”, ya “hard”.Aur .lower() isliye taaki capital letters me likha ho to bhi chale.

    if level == "easy":
        secret = random.randint(1, 10)
        max_attempts = 5     #Agar user ne “easy” bola:Computer 1 se 10 ke beech ek random number choose karega (yeh secret hai).User ko 5 chances milenge.Aise hi:Medium → 1–50 range aur 7 attemptsHard → 1–100 range aur 10 attemptsAgar kuch galat likha ho to default “easy” le lega.
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

    attempts = 0  #Yeh count karega user ne kitni baar guess kiya.Jaise hi user ek number input karega, attempts +1 ho jaayega.
    guessed = False   #Yeh ek flag hai jo batata hai — “user ne number guess kiya ya nahi”.start me False (matlab abhi guess nahi hua).
    
    while attempts < max_attempts:  #Yeh loop tab tak chalega jab tak user ke attempts khatam nahi hote.Jaise “5 chances” diye gaye ho to 5 baar ye chalega.
        guess = int(input("Enter your guess: "))  #Yeh user se ek number input leta hai.Input string hota hai, isliye int() lagaya gaya hai taaki use number me badla ja sake.
        attempts += 1 #Har guess ke baad attempts me +1 add ho jaata hai.
        
        if guess == secret:
            print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
            guessed = True
            break  #Agar user ka guess computer ke secret number ke barabar hai,congratulation message print hoga, aur loop break ho jaayega (game stop).
        elif guess < secret:
            print("📈 Too low!")  #Matlab user ka number secret se chhota hai → hint milta hai “Too low!”.
        else:
            print("📉 Too high!")   #Matlab user ka number secret se bada hai → hint “Too high!”.
    
    if not guessed:
        print(f"❌ Sorry, you couldn't guess the number. It was {secret}.")  #Agar guessed abhi bhi False hai → user haar gaya, aur correct number print hota hai.
    
    play = input("Do you want to play again? (yes/no): ")   #Game poochta hai: “Dobara khelna hai?”Agar user “yes” likhe to loop dubara chalega,Agar “no” likhe to game band ho jaayega.






#1   Random number generate karta hai
#2	User se level aur guess mangta hai
#3	Compare karta hai guess aur secret number
#4	Hint deta hai (Too high / Too low)
#5	Correct hone par Congratulations print karta hai
#6	Galat hone par correct number dikhata hai
#7	User se poochta hai dubara khelna hai ya nahi