#students management system

"""

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

"""


#OOP VERSION




class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self):
        roll = int(input("Roll: "))
        name = input("Name: ")
        marks = int(input("Marks: "))
        s = Student(roll, name, marks)
        self.students.append(s)

    def view_students(self):
        for s in self.students:
            print(s.roll, s.name, s.marks)

    def search_student(self):
        r = int(input("Enter roll: "))
        for s in self.students:
            if s.roll == r:
                print("Found:", s.name)
                return
        print("Not found")


manager = StudentManager()

while True:
    print("1 Add  2 View  3 Search  4 Exit")
    ch = int(input("Enter your choice:"))

    if ch == 1:
        manager.add_student()
    elif ch == 2:
        manager.view_students()
    elif ch == 3:
        manager.search_student()
    elif ch == 4:
        break
    else:
        print("Invalid choice!")
