# 1. CREATE THE CLASS (The Blueprint)
# We use the keyword 'class' followed by the name (Capitalized)
class Car:
    # This is a variable inside the class
    brand = "Toyota"
    model = "Fortuner"

# 2. CREATE THE OBJECT (The Real Car)
# We take the blueprint 'Car()' and store it in a variable 'my_car'
my_car = Car()

# 3. USE THE OBJECT
# We access the data using a dot (.)
print(my_car.brand)
print(my_car.model)