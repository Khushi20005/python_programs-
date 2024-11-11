 #Mid-Level Questions
"""Ques13. How can you create a class that inherits from another class?
 ○ Provide an example of inheritance in Python."""

#In Python, you can create a class that inherits from another class by specifying the parent class in parentheses after the name of the child class.
#This allows the child class to inherit all the attributes and methods of the parent class, and it can also have its own additional attributes or methods.

"""# Parent class
class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def description(self):
        return f"{self.color} {self.name}"

# Child class inheriting from Fruit
class Citrus(Fruit):
    def __init__(self, name, color, acidity):
        super().__init__(name, color)
        self.acidity = acidity

    def is_sour(self):
        return self.acidity > 5

# Creating instances
apple = Fruit("Apple", "red")
lemon = Citrus("Lemon", "yellow", 8)

# Testing methods
print(apple.description())      # Output: red Apple
print(lemon.description())      # Output: yellow Lemon
print(lemon.is_sour())          # Output: True"""

        #OR

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "This animal makes a sound."

# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):
        return "Woof! Woof!"

# Creating instances of the classes
animal = Animal("Generic Animal")
dog = Dog("Buddy")

# Testing the methods
print(animal.name)      # Output: Generic Animal
print(animal.speak())   # Output: This animal makes a sound.
print(dog.name)         # Output: Buddy
print(dog.speak())      # Output: Woof! Woof!        