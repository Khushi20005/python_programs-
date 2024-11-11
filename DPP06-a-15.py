"""Ques 15. What is encapsulation, and how is it achieved in Python?
 ○ Describe encapsulation and provide an example of private attributes"""

#Encapsulation is an object-oriented programming principle that restricts direct access to an object’s data and methods, 
# bundling related properties and methods together and protecting the internal state of an object. It hides the internal workings of a class from the outside,
#  allowing controlled access through public methods, which prevents unintended interference and enforces a clear structure.

#In Python, encapsulation is achieved through:

#Private Attributes: Attributes prefixed with underscores (like _attribute or __attribute) signal that they should not be accessed directly.
#Getter and Setter Methods: Public methods to get or set the value of private attributes safely.

"""class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance  # Private attribute

    # Getter method for balance
    def get_balance(self):
        return self.__balance

    # Setter method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Invalid deposit amount.")

    # Setter method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: ${amount}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

# Creating an instance of BankAccount
account = BankAccount(100)

# Accessing balance through public methods
print("Balance:", account.get_balance())  # Output: Balance: 100
account.deposit(50)                       # Output: Deposited: $50
account.withdraw(30)                      # Output: Withdrew: $30
print("Balance:", account.get_balance())  # Output: Balance: 120
# Trying to access private attribute directly (will raise an AttributeError)
# print(account.__balance)  # This will fail with an AttributeError"""

         #OR


class Person:
    def __init__(self, name, age):
        self.name = name            # Public attribute
        self.__age = age            # Private attribute

    # Getter method for age
    def get_age(self):
        return self.__age

    # Setter method to set age with validation
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Please enter a valid age.")

# Creating an instance of Person
person = Person("Alice", 25)

# Accessing public attribute directly
print("Name:", person.name)        # Output: Name: Alice

# Accessing private attribute via getter method
print("Age:", person.get_age())    # Output: Age: 25

# Modifying private attribute using setter method
person.set_age(30)
print("Updated Age:", person.get_age())  # Output: Updated Age: 30

# Attempting to set an invalid age
person.set_age(-5)                 # Output: Please enter a valid age.

# Trying to access private attribute directly (will raise an AttributeError)
# print(person.__age)  # This will fail with an AttributeError