#Finding Elements: Given the tuple letters = ('a', 'b', 'c', 'd'), check if
#the element 'e' is present in the tuple and print a message accordingly.
letters = ('a', 'b', 'c', 'd')
element = 'e'
if element in letters:
    print(f"'{element}' is present in the tuple.")
else:
    print(f"'{element}' is not present in the tuple.")