#Accessing Keys and Values: Given the dictionary student = {'name': 'John',
#'age': 22, 'course': 'Computer Science'}, print all the keys and values
student = {
    'name': 'john',
    'age': 22,
    'course': 'computer science'
}
print("Keys:", student.keys())
print("Values:", student.values())
for key, value in student.items():
    print(f"{key}: {value}")