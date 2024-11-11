"""Ques16. How do you create a class method in Python?
 ○ Explain the concept of a class method and give an example"""

#A class method is a method that is bound to the class and not to the instance of the class. 
# It is defined using the @classmethod decorator. A class method takes the class (cls) as its first argument instead of the instance (self), and
#  it can modify class-level attributes or call other class methods.

#Class methods are typically used for factory methods, i.e., methods that create instances of the class in a different way, 
# or when you want to perform some operations that affect the entire class, not just a particular instance.

#Creating a Class Method
#You define a class method by using the @classmethod decorator and by including cls as the first argument in the method.

class Car:
    # Class attribute
    wheels = 4
    
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    # Class method to access or modify class attributes
    @classmethod
    def change_wheels(cls, new_wheel_count):
        cls.wheels = new_wheel_count  # Modify the class-level attribute

    # Instance method to display details
    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Wheels: {self.wheels}")

# Creating an instance of Car
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

# Display info before modifying the class attribute
car1.display_info()  # Output: Make: Toyota, Model: Camry, Wheels: 4
car2.display_info()  # Output: Make: Honda, Model: Civic, Wheels: 4

# Using the class method to change the wheels count
Car.change_wheels(6)

# Display info after modifying the class attribute
car1.display_info()  # Output: Make: Toyota, Model: Camry, Wheels: 6
car2.display_info()  # Output: Make: Honda, Model: Civic, Wheels: 6