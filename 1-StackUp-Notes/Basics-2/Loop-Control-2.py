numbers=range(9) #[0,...,8]
# printing the numbers
for number in numbers:
	print(number)

# Using the break function
# Break stops the loop prematurely
for number in numbers:
	if number==5:
		break
	#will print [0,...,4]
	else:
		print(number)

# Using the pass function
# Pass allows code to pass through
for number in numbers:
	if number==7:
		pass # code will pass through
		print("number==7")
	else:
		print(number) # will print [0,1,....,number==7,8]

# Using the continue function
# Code goes back to the top and starts again
for number in numbers:
	if number==5:
		continue
	else:
		print(number) # The number 5 will not be printed