""" Write a python program that takes a string as input and returns a new string where each words first letter is capitalize 
(also known as "title case")for example, the input "hello world" should be return "Hello World". considered edge cases like multiple spaces between
words."""
def title_case(sentence):
    words = sentence.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)
print(title_case("hello world")) 