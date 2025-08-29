#Multiplication tables for 2–20
# Problem 3
for i in range(2, 21):
    with open(f"table_{i}.txt", "w") as f:
        for j in range(1, 11):
            f.write(f"{i} x {j} = {i*j}\n")
