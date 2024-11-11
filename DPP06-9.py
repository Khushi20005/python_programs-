#2. Inheritance
#  Create a base class Animal and a subclass Dog. The subclass should have 
# a method that overrides a method from the base class.
class Animal:
  def speak(self):
    return "Animal sound"
class Dog(Animal):
  def speak(self):
    return "Bark"
my_dog = Dog()
print(my_dog.speak()) # Should print "Bark"