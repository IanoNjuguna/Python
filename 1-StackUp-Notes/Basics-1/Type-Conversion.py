# A string
print("1")

# An integer
print(1)

# This statement prompts an error
print("1"+1)

# To correct this error, you have to covert either the string to an integer or the integer to a string
# Converting the string to an integer
print(int("1")+1)

# Converting the integer to a string
print(str(1)+"1")
print(str(2)+"2")
print(str(3)+"3")
print(str(4)+"4")
print(str(5)+"5")

# This statement prompts an error
print(int("10.00"))
# This is because the string is a float and in such a case, cannot be converted to an integer.
# To do it without an error:
print(float("10.00"))

# Converting a floating point to an integer
print(int(10.00))
print(int(10.534))

# To determine the data type you are working with:
print(type(float(10)))