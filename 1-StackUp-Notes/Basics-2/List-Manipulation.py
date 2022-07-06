# To count the number of items in a list, use the len() function. Example:

letters = ["a", "b", "c", "d", "e"]
# To get the an item in a list, consider:
# "a", "b", "c", "d", "e"
#  0    1    2    3    4
# -5   -4   -3   -2   -1
print(len(letters))

# To add additional items in a list, use .append()
# syntax; yourlist.append(newitem)
# everytime you append, you are adding to the end of the list
letters = ["a", "b", "c", "d", "e"]
print(letters)
letters.append("z")
print(letters)

# To remove items at the back of a list, use .pop()
# syntax; yourlist.pop()
letters = ["a", "b", "c", "d", "e"]
print(letters)
popped_item = letters.pop()
print(popped_item)
letters.pop()
print(letters)


# To store item that has been popped:
popped_item = letters.pop()
print(popped_item)
#This is useful when working with lists and you want to store removed items

# To remove items from a specific index in a list:
letters.pop(1)
print(letters)