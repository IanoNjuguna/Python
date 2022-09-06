# Tuples are immutable containers where you can store your values
# immutable=can't be changed
# Unlike lists, they are held in round brackets()
# Useful when storing immutable values
example_tuple=("a","b","c","d","e")
print(example_tuple)

# They can be manipulated like lists but ONLY in cases where they aren't changed. Thus, they canNOT be appended, popped, but they can be subset, sliced, counted etc
# Example:
print(len(example_tuple))#counting
print(example_tuple + ("f","g","h"))#Adding two tuples
print(example_tuple[2])#Retrieving

# You can turn lists to a tuple by using the tuple function:
example_list=[1,2,3,4,5]
print(tuple(example_list))