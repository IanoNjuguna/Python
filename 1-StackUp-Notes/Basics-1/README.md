# Basics-1

This directory contains all the code I wrote during the Basics-1 track.

## 1. [Hello World](Programming-In-Python\1-StackUp-Notes\Basics-1\Hello-World.py)

Traditionally when learning a new programming language, the first thing is to print out the ```Hello World``` statement.

### Why is this so?

    In my view, it is because:
        * the print function is a simple function from the Python standard library.
        * the print function is used to print any type of data or a result from any operation on the screen.
        * the print function is used for testing purposes.

 As with most things in programming, there are a myriad of possible answers to this query. Here are [some samples from the social media site, Quora](https://www.quora.com/Why-do-we-start-with-the-Hello-World?share=1)

## 2. Commenting

Commenting code is useful for documentation purposes and code readability.
In Python, comments are preceded by the ```#``` symbol for single-line comments and in between the ````""" """``` symbol(s) for multi-line comments.

## 3. Troubleshooting

Whenever an error message appears, use it to find the cause of the error and how it can be resolved.
To do this, you can Google, read docs or consult a fellow dev.

## 4. [Variables](Programming-In-Python\1-StackUp-Notes\Basics-1\Variables.py)

### What is a variable?

A variable is an area in memory that is used to store data.
In Python, variables are assigned by declaring the variable and assigning a value to it by using the ```=``` operator.

#### Variable Names

A variable can have a short name (```z``` or ```a```) or a more descriptive name (```age```, ```songname```, ```total-area```)
The following are the rules that guide allocating name to Python Variables:

    * A variable MUST start with a letter or the underscore character

    * A variable name can NOT start with a number

    * A variable name can ONLY contain alpha-numeric characters and underscores ( A - Z, 0 - 9 and _ )

    * Variable names are CASE SENSITIVE ( Age != age )

## [Mathematical/Arithmetic Operators](Programming-In-Python\1-StackUp-Notes\Basics-1\Mathematical-Operators.py)

### addition

Use the ```+``` operator.

### subtraction

Use the ```-``` operator

### multiplication

Use the ```*``` operator

### division

Use the ```\``` operator

### modulus

Also called ```mod```.
The ```%``` is called the ```modulo operation```.

In Mathematics and computing, modulus is the remainder of the euclidean division^[1] of one number by another.
For any number ```s```, the value of ```y % s``` is always less that ```s``` itself.

For instance, ```4``` divided by ```2``` equals ```2``` but it remains ```0```. Here, ```4 / 2 = 2``` and ```4 % 2 = 0```.
In another instance, ```9``` divided by ```4``` equals ```2``` but it remains ```1```. Here, ```9 / 4 = 2``` and ```9 % 4 = 1```.


### CAVEAT

The mathematical operations in Python are subject to the rules of Mathematical Operations.

[1] Source: [Euclidean Division](https://en.wikipedia.org/wiki/Euclidean_division)