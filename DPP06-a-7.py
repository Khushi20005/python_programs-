"""Ques 7. What is an instance attribute?
 ○ Explain the difference between instance attributes and class attributes"""

#An instance attribute is a variable defined within an instance of a class. Each instance of the class has its own separate copy of the instance attributes, meaning they can hold different values for each object created from the class.

#Key Characteristics of an Instance Attribute:
#Defined in the __init__ Method: Instance attributes are typically set within the __init__ method, which initializes the attributes with specific values for each instance.
#Unique to Each Instance: Each object has its own unique set of instance attributes. Changing the value of an instance attribute in one object does not affect other instances.
#Accessed via the Instance: Instance attributes are usually accessed or modified through the specific instance of the class.

#Difference Between Instance Attributes and Class Attributes
#Feature	Instance Attributes	Class Attributes
#Definition Location	Defined inside the __init__ method	Defined directly within the class body
#Scope	Unique to each instance	Shared across all instances of the class
#Modification Impact	Modifying an instance attribute affects only that instance	Modifying a class attribute affects all instances
#Typical Usage	Used for attributes that vary per object	Used for attributes that remain constant or need to be shared across all instances