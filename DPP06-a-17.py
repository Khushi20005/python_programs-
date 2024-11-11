"""Ques17. What is the difference between a class method and a static method?
 ○ Compareclass methods and static methods with code examples"""

#Both class methods and static methods are defined inside a class, but they differ in how they are called and what they can access. Here's a comparison:

#Class Method:
#Definition: A class method takes the class as its first argument (cls), which allows it to access and modify class-level attributes.
#Purpose: It is used to operate on class-level data or to create alternate constructors.
#Decorator: @classmethod
#Static Method:
#Definition: A static method does not take self or cls as its first argument. It behaves like a regular function but belongs to the class's namespace.
#Purpose: It is used for utility functions that do not require access to the class or instance but are related to the class's functionality.
#Decorator: @staticmethod

class Car:
    wheels = 4  # Class attribute

    def __init__(self, make, model):
        self.make = make
        self.model = model

    # Class method
    @classmethod
    def set_wheels(cls, wheel_count):
        cls.wheels = wheel_count  # Modifies the class-level attribute

    # Static method
    @staticmethod
    def is_valid_car(make, model):
        return bool(make) and bool(model)  # Validates car data (does not need access to instance or class)

    # Instance method to display car information
    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Wheels: {self.wheels}")


# Creating instances
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

# Using class method to change class-level attribute (wheels)
car1.display_info()  # Output: Make: Toyota, Model: Camry, Wheels: 4
car2.display_info()  # Output: Make: Honda, Model: Civic, Wheels: 4

# Using class method to modify the class attribute (wheels)
Car.set_wheels(6)

# Display info after modifying the class attribute
car1.display_info()  # Output: Make: Toyota, Model: Camry, Wheels: 6
car2.display_info()  # Output: Make: Honda, Model: Civic, Wheels: 6


# Using static method to check if car data is valid
print(Car.is_valid_car("Toyota", "Camry"))  # Output: True
print(Car.is_valid_car("", "Civic"))        # Output: False

#Key Differences:
"""Class Method:
The first argument is cls, which refers to the class itself.
It can modify class-level attributes or call other class methods.
Used when you need to interact with the class-level data or create class instances (alternate constructors)."""
#Static Method:
"""It doesn't take cls or self as its first argument.
It can't modify instance-level or class-level data, and is used for utility functions that are related to the class but don't need to access any class or instance data.
It is independent of the class and instance."""
#Use Case Summary:
"""Class Methods are commonly used for modifying class-level attributes or providing alternate constructors.
Static Methods are used for utility functions that are logically related to the class but do not interact with the class or its instances."""





