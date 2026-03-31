from storage import load_students, save_students
from student import Student

def show_menu():
    print("\n==== Student Manager====")
    print("1. Add student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Delete Student")
    print("0. Exit")
    
def add_student(student):
    name = input("Enter name: ").strip()
    
    try:
        marks = int(input("Enter marks: "))
    except ValueError:
        print("marks should be a number!")
        return
    
    student.append(Student(name, marks))
    print("Student added!")
    
def view_students(student):
    if not student:
        print("No data available")
        return
    
    print("\n--- Student List---")
    for i, s in enumerate(student, start=1):
        print(f"{i}. {s.name} - {s.marks}")
        
        
def search_student(students):
    keyword = input("Enter name to search: ").lower()
    
    found = False
    for s in students:
        if keyword in s.name.lower():
            print(f"found: {s.name} - {s.marks}")
            found = True
            
    if not found:
        print("No student found")
        
        
def delete_student(students):
    name = input("Enter name to delete: ").lower()
    
    for s in students:
        if s.name.lower() == name:
            students.remove(s)
            print("Delete successfully")
            return
        
        print("Student not found")
        
def main():
    students = load_students()
    
    while True:
        show_menu()
        choice = input("Choose option: ")
        
        if choice == "1":
            add_student(students)
            
        elif choice == "2":
            view_students(students)
            
        elif choice == "3":
            search_student(students)
            
        elif choice == "0":
            save_students(students)
            print("Data saved. Exiting...")
            break
        
        else:
            print("Invalid choice, try again")
            
if __name__=="__main__":
   main() 
   
            
    