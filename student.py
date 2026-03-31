class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"{self.name},{self.marks}"

    @staticmethod
    def from_string(data):
        try:
            name, marks = data.strip().split(",")
            marks = int(marks)
            return Student(name, marks)
        except:
            return None