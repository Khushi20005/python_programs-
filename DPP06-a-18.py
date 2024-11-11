"""Ques18. How can you override a method in a subclass?
 ○ Write an example showing method overriding in inheritance."""

#Method Overriding in Inheritance
#Method overriding occurs when a subclass provides a specific implementation for a method that is already defined in its superclass. 
# The subclass's version of the method will be called instead of the method from the parent class when the method is invoked on an instance of the subclass.

#In Python, to override a method, you define the method in the subclass with the same name and parameters as the one in the parent class.

# Parent class
class Animal:
    def speak(self):
        print("The animal makes a sound")

# Subclass overriding the speak method
class Dog(Animal):
    def speak(self):
        print("The dog barks")

# Subclass overriding the speak method
class Cat(Animal):
    def speak(self):
        print("The cat meows")

# Create instances of Dog and Cat
dog = Dog()
cat = Cat()

# Calling the overridden method
dog.speak()  # Output: The dog barks
cat.speak()  # Output: The cat meows

# Create an instance of the parent class
animal = Animal()
animal.speak()  # Output: The animal makes a sound