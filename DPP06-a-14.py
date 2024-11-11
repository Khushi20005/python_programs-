"""Ques14. What is polymorphism in the context of classes?
 ○ Explain polymorphism and give a code example."""

#Polymorphism in the context of classes refers to the ability of different classes to be treated as instances of the same superclass, 
# even if they implement their own versions of methods. 
# In other words, polymorphism allows objects of different types to be accessed through the same interface, 
# enabling methods with the same name to act differently based on the object calling them. 
# This is especially useful in object-oriented programming because it allows for flexible and reusable code.

# Parent class
class Bird:
    def fly(self):
        return "Some birds can fly."

# Child class 1
class Parrot(Bird):
    def fly(self):
        return "Parrots can fly high."

# Child class 2
class Penguin(Bird):
    def fly(self):
        return "Penguins cannot fly."

# Function that demonstrates polymorphism
def bird_flight_test(bird):
    print(bird.fly())

# Creating instances
parrot = Parrot()
penguin = Penguin()

# Testing polymorphism
bird_flight_test(parrot)   # Output: Parrots can fly high.
bird_flight_test(penguin)  # Output: Penguins cannot fly.