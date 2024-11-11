"""Ques20. How can you create a property in a class?
 ○ Explain how to use the property decorator to create a property and provide an
 example"""

#.Creating a Property in a Class Using the property Decorator
#In Python, a property allows you to define a method that behaves like an attribute. This provides a way to get, set, and delete an attribute in a controlled manner, without directly accessing or modifying the underlying attribute. Using the property decorator, you can define methods that are accessed like attributes but with additional logic.

#Steps to Create a Property:
"""1.Define a method in your class that you want to use as a property.
2.Use the @property decorator to mark the method as a property.
3.Optionally, define setter and deleter methods for the property if you want to allow modification or deletion of the property."""


class Circle:
    def __init__(self, radius):
        self._radius = radius  # Private attribute for radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def area(self):
        return 3.14 * (self._radius ** 2)

# Example usage
circle = Circle(5)

# Accessing the radius and area using property methods
print(circle.radius)  # Output: 5
print(circle.area)    # Output: 78.5 (3.14 * 5^2)

# Modifying the radius using the setter
circle.radius = 10
print(circle.area)    # Output: 314.0 (3.14 * 10^2)

# Trying to set a negative radius (will raise an exception)
# circle.radius = -5  # Uncommenting this line will raise ValueError

"""Key Points:
Property: The @property decorator is used to define a method that behaves like an attribute, enabling controlled access to data.
Setter Method: The @property_name.setter decorator allows you to define how the property can be modified.
Getter Method: The @property decorator defines the getter method for retrieving the value of the property.
Encapsulation: Properties allow you to encapsulate the logic for getting, setting, and deleting an attribute while maintaining a clean and intuitive interface for users of the class.
Benefits of Using Properties:
Encapsulation: Allows you to control how an attribute is accessed or modified while still giving the appearance of a simple attribute.
Data Validation: You can include validation logic in setter methods to ensure data consistency.
Read-Only Attributes: If you only provide a getter method and not a setter, the property can be made read-only."""