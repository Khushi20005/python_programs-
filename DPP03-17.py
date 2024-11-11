#Dictionary Iteration: Write a loop to iterate over the dictionary {'A': 90, 'B': 80,
#'C': 70} and print each key-value pair.
grades = {
    'A': 90,
    'B': 80,
    'C': 70
}
for key, value in grades.items():
    print(f"Grade: {key}, Score: {value}")