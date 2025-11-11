tasks = []

while True:
    print("\n📝 To-Do List Menu")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print("✅ Task added!")
    elif choice == "2":
        print("\nYour Tasks:")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")
    elif choice == "3":
        num = int(input("Enter task number to remove: "))
        del tasks[num - 1]
        print("❌ Task removed!")
    elif choice == "4":
        print("👋 Exiting To-Do List. Bye!")
        break

