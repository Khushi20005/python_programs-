"""Ques11. What does the self keyword represent?
 ○ Explain the role of the self keyword in class methods"""

#The self keyword in Python is a reference to the current instance of the class. 
# It is used as the first parameter in instance methods to allow each method to access and manipulate attributes and other methods of that particular instance.

#Role of the self Keyword:
##Access Instance Attributes: Using self, methods can access the instance’s attributes. 
# This allows each object created from the class to hold its own data independently of other instances.
#Differentiate Between Class and Instance Variables: self helps to differentiate between attributes and methods that belong to the instance
#  (i.e., unique to each object) and those that are shared by all instances (class attributes).
#Enable Method Calls Within the Class: When calling another method of the class from within a method, self allows you to call it on the current instance.