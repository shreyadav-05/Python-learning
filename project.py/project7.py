#students management system



students = []

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        roll = int(input("Enter roll number: "))
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))
        
        student = {
            "roll": roll,
            "name": name,
            "marks": marks
        }
        
        students.append(student)
        print("Student added successfully!")

    elif choice == 2:
        if not students:
            print("No students found.")
        else:
            for s in students:
                print("Roll:", s["roll"])
                print("Name:", s["name"])
                print("Marks:", s["marks"])
                print("-----------")

    elif choice == 3:
        search_roll = int(input("Enter roll number to search: "))
        found = False
        
        for s in students:
            if s["roll"] == search_roll:
                print("Student Found!")
                print("Name:", s["name"])
                print("Marks:", s["marks"])
                found = True
                break
        
        if not found:
            print("Student not found.")

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")



