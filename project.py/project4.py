# to do list

tasks = []

while True:
    print("\n  To-Do List Menu")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        f = open("tasks.txt", "a")
        f.write(task + "\n")
        f.close()
        print("✅ Task added!")

    elif choice == "2":
        print("\nYour Tasks:")
        f = open("tasks.txt", "r")
        lines = f.readlines()
        f.close()
        for i, t in enumerate(lines, 1):
            print(f"{i}. {t.strip()}")  # file ke tasks print honge

    elif choice == "3":
        f = open("tasks.txt", "r")
        lines = f.readlines()
        f.close()

        print("\nYour Tasks:")
        for i, t in enumerate(lines, 1):
            print(f"{i}. {t.strip()}")

        num = int(input("Enter task number to remove: "))

        
        del lines[num - 1]

        f = open("tasks.txt", "w")
        for t in lines:
            f.write(t)
        f.close()

        print("❌ Task removed successfully!")

    elif choice == "4":
        print("👋 Exiting To-Do List. Bye!")
        break

    





#Step	 Action	               Concept
#1	     Empty list	           Data store
#2	     While loop	           Program repeat
#3	     Menu print	           User options
#4	     Input choice	       Decide what to do
#5	     Add task	           append()
#6	     View task	           for loop + enumerate()
#7	     Remove task	       del
#8	     Exit	               break