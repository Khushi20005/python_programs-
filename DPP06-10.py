#3. Polymorphism
#  Create two classes Cat and Dog, both having a method speak.
# Demonstrate polymorphism by calling the method on both objects.
class Cat:
  def speak(self):
    return "Meow"
class Dog:
   def speak(self):
      return "Woof"
      def animal_sound(animal):
         print(animal.speak())
my_cat = Cat()
my_dog = Dog()
animal_sound(my_cat) # Should print "Meow"
animal_sound(my_dog) # Should print "Woof"