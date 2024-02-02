import json

class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        if not self.students:
            print("No students available.")
        else:
            for student in self.students:
                print(f"ID: {student.student_id}, Name: {student.name}, Age: {student.age}, Grade: {student.grade}")

    def search_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def update_student(self, student_id, new_name, new_age, new_grade):
        student = self.search_student(student_id)
        if student:
            student.name = new_name
            student.age = new_age
            student.grade = new_grade
            print(f"Student information updated for ID {student_id}.")
        else:
            print(f"Student with ID {student_id} not found.")

    def delete_student(self, student_id):
        student = self.search_student(student_id)
        if student:
            self.students.remove(student)
            print(f"Student with ID {student_id} deleted.")
        else:
            print(f"Student with ID {student_id} not found.")

    def save_students_to_file(self, filename):
        data = [{"ID": student.student_id, "Name": student.name, "Age": student.age, "Grade": student.grade} for student in self.students]
        with open(filename, 'w') as file:
            json.dump(data, file)
        print("Student data saved to file.")

    def load_students_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.students = [Student(student["ID"], student["Name"], student["Age"], student["Grade"]) for student in data]
            print("Student data loaded from file.")
        except FileNotFoundError:
            print("File not found. No student data loaded.")

# Example usage with a simple menu:
student_system = StudentManagementSystem()

while True:
    print("\nMenu:")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Save Students to File")
    print("7. Load Students from File")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice == '1':
        student_id = int(input("Enter Student ID: "))
        name = input("Enter Student Name: ")
        age = int(input("Enter Student Age: "))
        grade = input("Enter Student Grade: ")
        student_system.add_student(Student(student_id, name, age, grade))

    elif choice == '2':
        student_system.display_students()

    elif choice == '3':
        search_id = int(input("Enter Student ID to search: "))
        found_student = student_system.search_student(search_id)
        if found_student:
            print(f"Student found - ID: {found_student.student_id}, Name: {found_student.name}, Age: {found_student.age}, Grade: {found_student.grade}")
        else:
            print(f"Student with ID {search_id} not found.")

    elif choice == '4':
        update_id = int(input("Enter Student ID to update: "))
        new_name = input("Enter new Name: ")
        new_age = int(input("Enter new Age: "))
        new_grade = input("Enter new Grade: ")
        student_system.update_student(update_id, new_name, new_age, new_grade)

    elif choice == '5':
        delete_id = int(input("Enter Student ID to delete: "))
        student_system.delete_student(delete_id)

    elif choice == '6':
        filename = input("Enter file name to save student data: ")
        student_system.save_students_to_file(filename)

    elif choice == '7':
        filename = input("Enter file name to load student data: ")
        student_system.load_students_from_file(filename)

    elif choice == '8':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 8.")
