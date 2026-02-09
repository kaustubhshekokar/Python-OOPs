class Instructor:
    followers=0

    def __init__(self, name, address) :
        self.name=name
        self.address=address

    #self.followers=0
    def display(self):
        print("Hi")

instructor_1=Instructor("Jenny", "Gurgaon")
print(instructor_1.name)
print(instructor_1.display())
#instructor_2=Instructor("Jiya", "Gurgaon")