

def print_table(num):                     # function define upar
    for i in range(1, 11):                # 1 to 10 loop
        result = num * i
        print(num, "x", i, "=", result)

play = "yes"                              # start condition

while play == "yes":                      # jab tak user chahe
    try:
        num = int(input("Enter number: "))    # user se number lena
        print_table(num)                      # function call
    except ValueError:
        print("⚠️ Please enter a valid number!")
        continue                            # loop ko dobara se start karega
    play = input("Do you want to play again? (yes/no): ").lower()
    
print("thank u for playing")