"""Ques 6. What is a class attribute?
 ○ Define a class attribute and give an example"""

#A class attribute is a variable that is shared across all instances of a class. Unlike instance attributes, which are defined in the _init_ method and unique to each object, class attributes are defined directly within the class body and have the same value for every instance of that class unless modified.

#Key Characteristics of a Class Attribute:
#Shared Across Instances: All instances of the class share the same value for a class attribute. 
# If the attribute is changed at the class level, the change is reflected across all instances.
#Accessed via Class or Instance: You can access class attributes using either the class name or an instance of the class.
#Typically Used for Constants: Class attributes are often used for data that remains constant across instances, 
# such as configuration settings, counters, or default values.
#Example of a Class Attribute:
#python
#Copy code
class Dog:
    species = "Canis lupus familiaris"  # This is a class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

# Creating instances of Dog
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# Accessing the class attribute
print(dog1.species)      # Output: Canis lupus familiaris
print(dog2.species)      # Output: Canis lupus familiaris
print(Dog.species)       # Output: Canis lupus familiaris

# Accessing instance attributes
print(dog1.name)         # Output: Buddy
print(dog2.name)         # Output: Max