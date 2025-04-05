class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "D"

    def display_info(self):
        print(f"Student: {self.name}, Marks: {self.marks}, Grade: {self.get_grade()}")


student1 = Student("John", 85)
student2 = Student("Emma", 92)


student1.display_info()
student2.display_info()
