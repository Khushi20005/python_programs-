"""Ques2. Howdoyoudefine a class in Python?
 ○ Write a simple example of a class definition."""

#In Python, a class is defined using the class keyword, followed by the class name and a colon. Inside the class, we define methods (functions) and attributes (variables) that belong to the class. The _init_ method is a special method that initializes the object's attributes and is automatically called when an object of the class is created.

#Here's a simple example of a class definition:

#python
class Dog:
    # Initialization method
    def __init__(self, name, age):
        self.name = name  # Attribute
        self.age = age    # Attribute

    # Method to display dog's details
    def display_info(self):
        print(f"{self.name} is {self.age} years old.")
    
    # Method to make the dog bark
    def bark(self):
        print("Woof! Woof!")

dog1 = Dog("Buddy", 3)

# Call methods to test
dog1.display_info()  # Should print: Buddy is 3 years old.
dog1.bark()          # Should print: Woof! Woof!

#Explanation
#_init_ method: This is the initializer method that sets up the initial values for the name and age attributes.
#Attributes: self.name and self.age are instance attributes, which are unique to each instance (object) of the Dog class.
#Methods: display_info and bark are methods that operate on instances of the class.

