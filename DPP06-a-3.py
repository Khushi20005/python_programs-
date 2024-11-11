"""Ques3. What is an object in Python?
 ○ Describe what an object is in the context of classes"""

#In Python, an object is a fundamental building block that represents an instance of a class. 
# Classes serve as blueprints or templates for creating objects, defining the properties (attributes) and behaviors (methods) that each instance of that class will have. Here’s a breakdown of objects and their context within classes:

#Instance of a Class: An object is a concrete instance created from a class. 
# For example, if we define a class Dog, each Dog instance created using this class (such as Dog() or my_dog = Dog()) is an object.

#Attributes and Methods: Objects have attributes (data) and methods (functions) defined by their class. 
# When an object is created, it can have unique values for its attributes, but it shares the method definitions with other instances of the same class. For example, every Dog object might have an attribute name and a method bark(), but each Dog instance can have a different name while sharing the behavior of bark().

#Encapsulation: Objects in Python encapsulate data and functionality together, meaning that an object can manage its own state and behavior. 
# The concept of encapsulation is fundamental to Object-Oriented Programming (OOP) and allows objects to interact with each other through well-defined interfaces.

#Identity and State: Each object has a unique identity (address in memory), and it can hold a state, which is represented by the values of its attributes. 
# Even if two objects are created from the same class and have the same attribute values, they are distinct entities in memory.