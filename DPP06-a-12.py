"""Ques12. Can you create a class without any attributes or methods?
 ○ Discuss whether it’s possible and provide a brief code example"""

#Yes, you can create a class in Python without any attributes or methods. This is sometimes called an "empty class," and
#it can be useful as a placeholder or base class. In Python, you can create an empty class by using the pass keyword, 
#which is used as a placeholder for code blocks that you want to leave empty.

"""class MyEmptyClass:
    pass

# Creating an instance of the empty class
obj = MyEmptyClass()

# Checking the type of obj
print(type(obj))  # Output: <class '__main__.MyEmptyClass'>"""

      #OR


class Placeholder:
    pass

# Creating an instance of the Placeholder class
example = Placeholder()

# Adding an attribute dynamically
example.attribute = "I am an attribute"

# Printing the dynamically added attribute
print(example.attribute)  # Output: I am an attribute