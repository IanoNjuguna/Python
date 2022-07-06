letters = ["a", "b", "c", "d", "e"]
# "a", "b", "c", "d", "e"
#  0    1    2    3    4
# -5   -4   -3   -2   -1

# To retrieve the first 3 items:
print(letters[:3])

# To retrieve the first two items:
print(letters[:2])

# To retrieve the middle items:
# We will print out items starting at index 2 and end before the beginning of index 3
print(letters[2:4])
# By having a number at both sides of the colon, we can specify which is the start index to the {end index + 1}
# The end index is not printed
# syntax; list[start_index:{end_index + 1}]

# To retrieve items at a particular index all the way to the end of the list:
print(letters[1:])

# Negative indexing is possible but highly unrecommended