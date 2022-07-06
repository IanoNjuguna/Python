# example of a function that when invoked prints Hello World
# this kind of function does not require any keywords in the center of the brackets
def helloworld():
    return "Hello world"

print(helloworld())

# building a function that takes in an argument
# this kind of function prints Hello + whatever string is assigned to the function so it's important to put keywords in the center of the brackets
def hello(sentence):
    return "Hello" + " " + sentence

print(hello("Reader"))

# doing multiple arguments in a function
# this function does arithmetic
def addTwo(a,b):
    return a + b

print(addTwo(150, 200))