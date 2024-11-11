# Static Methods
# Create a class MathUtils with a static method add that takes two
# numbers and returns their sum.
class MathUtils:
  @staticmethod
  def add(a, b):
    return a + b
print(MathUtils.add(5, 10)) # Should print 15