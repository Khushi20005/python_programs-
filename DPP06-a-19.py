"""Ques19. What are magic methods in Python?
 ○ Define magic methods and provide examples of commonly used ones (e.g.,
 __str__, __repr__)."""

#Magic methods (also called dunder methods due to their double underscores) are special methods in Python that allow you to define the behavior of objects for built-in operations. 
# These methods enable objects to interact with Python's syntax in a more intuitive or natural way, and they are automatically called when certain operations are performed on objects.

#Magic methods are prefixed and suffixed with double underscores (e.g., __init__, __str__, __repr__), and they allow you to define how objects behave with operators, functions, and built-in methods.

#Commonly Used Magic Methods
#Here are a few of the most commonly used magic methods:

#__str__(self):

#Defines the string representation of an object when using str() or when the object is printed using print().
#It should return a human-readable string representation of the object.
#Example:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."

person = Person("Alice", 30)
print(person)  # Output: Alice is 30 years old.

#__repr__(self):

#Defines a formal string representation of an object that is ideally unambiguous. This method is used by the repr() function.
#It should return a string that could be used to recreate the object (if possible).
#Example:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

person = Person("Alice", 30)
print(repr(person))  # Output: Person('Alice', 30)
