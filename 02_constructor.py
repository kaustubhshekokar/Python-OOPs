class Student:
    # This magic method runs the moment a new student is created
    def __init__(self, name, branch, cgpa):
        self.name = name       # 'self' is like saying "MY name"
        self.branch = branch
        self.cgpa = cgpa
        print(f"Success: Record created for {self.name}")

    def intro(self):
        print(f"I am {self.name} from {self.branch} with {self.cgpa} CGPA.")

# Creating unique students
s1 = Student("Kaustubh", "ENTC", 8.03)
s2 = Student("Aditya", "CS", 9.5)

s1.intro()
s2.intro()