class Instructor():
    follower=0
    def __init__(self,name,address):
        self.nam=name
        self.add=address

    """def display(self):
        print("HI")
        print(f"Hi,I am {self.nam}")"""

    def display(self,subject):
        
        print("HI")
        print(f"Hi,I am {self.nam},I teach {subject}")    
    def follower_count(self,name):
        self.follower +=1    


inst1=Instructor("jenny","Ramu")
#print(inst1.nam)
print(inst1.display("Python"))
#inst1.display()
inst1.follower_count("King")
print(inst1.follower)




        