# Sets are types of arrays that do not allow for duplicates.
# Example:
example_set={"a","b","a"}

print(example_set)

# To some degree, there are similarities between sets and lists.
# To convert list to sets
example_list=[1,2,3,3,3,3,4,4,5]

print(set(example_list))

# Functions used in lists apply in sets to some extent.
# Example:
# To find the length of a set:

print(len(example_set))

# To add an item to the set:
example_set.add("h")

print(example_set)
# To remove an item in the set:
example_set.remove("a")

print(example_set)

# Sets are useful when you want to find the differences or
# common items between two different arrays
# For example:
example_set_2={"z","d","c","a"}

print(example_set_2)

# To compare the two sets:

print(example_set & example_set_2)

# To subtract sets so that you can find the common elements:

print(example_set - example_set_2)

# The order in which you subtract sets matters:

print(example_set_2 - example_set)
