#Accessing Attributes
class Person:
  def __init__(self, name):
   self.name = name
p = Person("Alice")
print(p.name) # Should print Alice