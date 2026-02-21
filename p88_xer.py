class Circle:
    pi=3.14 #class object attribut for all
    def __init__(self,radius=5):
        self.radius=radius
        self.area=Circle.pi*radius*radius

    def circumference(self):
        return 2* self.pi * self.radius
    def get_area(self):
        return self.pi*self.radius*self.radius
circle1=Circle(7)        
print(circle1.get_area())
print(circle1.area)


















