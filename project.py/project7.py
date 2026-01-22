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


"""

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


"""





#Train Booking System (Python – OOP)

"""

# Train class (sirf data)
class Train:
    def __init__(self, train_no, name, seats):
        self.train_no = train_no
        self.name = name
        self.seats = seats


# Booking system class (logic)
class BookingSystem:
    def __init__(self):
        self.trains = []

    def add_train(self):
        train_no = int(input("Enter Train Number: "))
        name = input("Enter Train Name: ")
        seats = int(input("Enter Total Seats: "))

        train = Train(train_no, name, seats)
        self.trains.append(train)

        print("✅ Train added successfully!")

    def view_trains(self):
        if not self.trains:
            print("❌ No trains available.")
        else:
            print("\nAvailable Trains:")
            for t in self.trains:
                print(f"Train No: {t.train_no}, Name: {t.name}, Seats: {t.seats}")

    def book_ticket(self):
        train_no = int(input("Enter Train Number to book ticket: "))

        for t in self.trains:
            if t.train_no == train_no:
                if t.seats > 0:
                    t.seats -= 1
                    print("🎟️ Ticket booked successfully!")
                else:
                    print("❌ No seats available.")
                return

        print("❌ Train not found.")


# Main program
system = BookingSystem()

while True:
    print("\n--- Train Booking System ---")
    print("1. Add Train")
    print("2. View Trains")
    print("3. Book Ticket")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        system.add_train()
    elif choice == 2:
        system.view_trains()
    elif choice == 3:
        system.book_ticket()
    elif choice == 4:
        print("🙏 Thank you for using Train Booking System")
        break
    else:
        print("❌ Invalid choice! Try again.")

"""



#Hotel Reservation System (Python – OOP)


# Room class (sirf data)
class Room:
    def __init__(self, room_no, room_type, price, is_available=True):
        self.room_no = room_no
        self.room_type = room_type
        self.price = price
        self.is_available = is_available


# Hotel class (logic handle karta hai)
class Hotel:
    def __init__(self):
        self.rooms = []

    def add_room(self):
        room_no = int(input("Enter Room Number: "))
        room_type = input("Enter Room Type (Single/Double): ")
        price = int(input("Enter Price per day: "))

        room = Room(room_no, room_type, price)
        self.rooms.append(room)

        print("✅ Room added successfully!")

    def view_rooms(self):
        if not self.rooms:
            print("❌ No rooms available.")
            return

        print("\nAvailable Rooms:")
        for r in self.rooms:
            status = "Available" if r.is_available else "Booked"
            print(f"Room No: {r.room_no}, Type: {r.room_type}, Price: {r.price}, Status: {status}")

    def book_room(self):
        room_no = int(input("Enter Room Number to book: "))

        for r in self.rooms:
            if r.room_no == room_no:
                if r.is_available:
                    r.is_available = False
                    print("🏨 Room booked successfully!")
                else:
                    print("❌ Room already booked.")
                return

        print("❌ Room not found.")

    def checkout_room(self):
        room_no = int(input("Enter Room Number for checkout: "))

        for r in self.rooms:
            if r.room_no == room_no:
                if not r.is_available:
                    r.is_available = True
                    print("✅ Checkout successful!")
                else:
                    print("❌ Room is already available.")
                return

        print("❌ Room not found.")


# Main Program
hotel = Hotel()

while True:
    print("\n--- Hotel Reservation System ---")
    print("1. Add Room")
    print("2. View Rooms")
    print("3. Book Room")
    print("4. Checkout Room")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        hotel.add_room()
    elif choice == 2:
        hotel.view_rooms()
    elif choice == 3:
        hotel.book_room()
    elif choice == 4:
        hotel.checkout_room()
    elif choice == 5:
        print("🙏 Thank you for using Hotel Reservation System")
        break
    else:
        print("❌ Invalid choice! Try again.")
