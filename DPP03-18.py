#Dictionary Comprehension: Create a dictionary where the keys are numbers from 1 to
#5 and the values are their squares using dictionary comprehension.
squares = {x: x**2 for x in range(1, 6)}
print(squares)