#Immutability: Why can’t we modify the elements of a tuple? Demonstrate an example of
#an error that occurs when trying to modify a tuple.
"""my_tupple=(1,2,3)
my_tupple[1]=4
print(my_tupple)"""

 #OR
my_tuple = (1, 2, 3)
try:
    # Attempting to modify an element of the tuple
    my_tuple[0] = 10
except TypeError as e:
    print(f"Error: {e}")