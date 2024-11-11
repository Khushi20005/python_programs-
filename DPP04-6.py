# Write a Python function find_greater_than(lst, n) that accepts a list lst of
#numbers and a number n. The function should return a new list containing only the
#numbers greater than n
def find_greater_than(lst, n):
 # This function takes a list lst of numbers and a number n as input
 # It returns a new list containing only the numbers greater than n
    return [num for num in lst if num > n] # List comprehension filters numbers greater than n

numbers = [1, 5, 8, 12, 3]
result = find_greater_than(numbers, 5)
print(result)  # Output: [8, 12]