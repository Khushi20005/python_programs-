"""Ques4. How do you create an object from a class?
 ○ Showhow to create an object of a class with a code example"""

#To create an object from a class in Python, you need to:

#Define a class with an __init__ method (also known as a constructor) to initialize attributes.
#Instantiate the class by calling it with any necessary arguments.
#Here’s a step-by-step example:

#python
#Copy code
# Step 1: Define the class
class Person:
    def __init__(self, name, age):
        self.name = name  # Initialize name attribute
        self.age = age    # Initialize age attribute

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Step 2: Create an object of the class
person1 = Person("Alice", 30)  # 'person1' is an instance of 'Person'

# Accessing attributes and methods
print(person1.name)          # Output: Alice
print(person1.age)           # Output: 30
print(person1.greet())       # Output: Hello, my name is Alice and I am 30 years old.
#Explanation:
#Person is the class, which serves as a blueprint.
#person1 = Person("Alice", 30) creates an object of the Person class, called person1, with name set to "Alice" and age set to 30.
#person1.name, person1.age, and person1.greet() demonstrate accessing the object's attributes and calling its method.
#This is how you create an object and interact with its attributes and methods.