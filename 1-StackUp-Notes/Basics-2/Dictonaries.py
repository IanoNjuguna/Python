# Dictionaries are flexible, versatile structures that contain a key and a value.
# An associative array where the key contains and an associative value to it.
# syntax is: {key:value}
# They are useful when storing multiple kinds of information within a single variable.
# Consider a variable {john}, Name:John Smith, Age:18
john={"name":"John Smith","age":18}
print (john)
# To add additional info:
john["country"]="Singapore"
print(john)
# To retrieve a value, use a key:
print(john['name'])
# Printing a non-existent key results in error, to see available keys:
print(john.keys())
# To see available values:
print(john.values())
# A dictionary can store all kinds of data types:[Boolean, Int, String, Float]
john['hasKids']=True    #Boolean
john['favColors']=['black','white','red']   #String
john['Balance']=500,674,723.3968    #Float
print(john)