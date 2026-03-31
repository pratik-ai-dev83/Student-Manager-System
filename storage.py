import os
from student import Student

FILE_NAME ="data.txt"


def load_students():
    students = []
    
    if not os.path.exists(FILE_NAME):
        return students
    
    with open(FILE_NAME,"r") as f:
        for line in f:
            if line.strip() == "":
                continue
            
            student = Student.from_string(line)
            
            if student:
                students.append(student)
                
    return students

def save_students(students):
    with open(FILE_NAME, "W") as f:
        for s in students:
            f.write(str(s) + "\n")