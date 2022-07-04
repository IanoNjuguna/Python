# if statement

# if a particular condition is met, then the code is executed. For instance:

if True:
    print("This is True")

# in the above case, "This is true" is printed because the condition stipulated by the if statement is met.

if False:
    print("This is True")

# in the above case, nothing is printed because the condition stipulated by the if statement is not met.

is_raining=True

if is_raining:
    print("Let's grab an umbrella")


# else statement

# if the if condition is not met, the else condition takes over. For instance:

is_raining=False

if is_raining:
    print("Let's grab an umbrella")

else:
    print("No need to bring umbrella")

# in the above case, "No need to bring umbrella" is printed because the condition in the if statement is not met thus the condition in the else statement is met.

# elif statement
# elif stands for else if
# used when you have additional conditions to consider other than the if and else conditions
# in our case, when the weather is hot, we'll need to bring an umbrella as well.
# This is akin to introducing additional if statements

is_raining=False
is_sunny=True

if is_raining:
    print("Let's grab an umbrella")

elif is_sunny:
    print("Let's go grab an umbrella")

else:
    print("No need to bring umbrella")

# in the above case, "Let's go grab an umbrella" is printed because since the code runs from top to bottom, once the elif statement is met it executes the code immediately and the code stops running

# if we expect to bring an umbrella when it's both rainy and sunny, we use the or operator in the following manner
# in doing this, the elif statement becomes redundant

is_raining=False
is_sunny=True

if is_raining or is_sunny:
    print("Let's grab an umbrella")

else:
    print("No need to bring umbrella")