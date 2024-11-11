"""Ques 8. How do you access an attribute of an object?
 ○ Provide an example of how to access an attribute from an object"""


#To access an attribute of an object in Python, you use dot notation. This involves specifying the object's name followed by a dot (.) and the attribute's name.

#Syntax:
#python
#Copy code
#object_name.attribute_name
#Here’s an example to demonstrate how to access an attribute of an object:

#python
#Copy code
class Person:
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

# Creating an object of the Person class
person1 = Person("Alice", 30)

# Accessing attributes
print(person1.name)  # Output: Alice
print(person1.age)   # Output: 30
#Explanation:
#Creating the Object: We create an instance of the Person class called person1 with name set to "Alice" and age set to 30.
#Accessing Attributes: Using person1.name and person1.age, we access the name and age attributes of person1.