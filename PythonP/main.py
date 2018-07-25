import funClasses, rectangularFigures
from funClasses import DEFAULT_FLOAT_FORMAT

# FUNCTIONS
def process_selection(xObject, ignore = False):
	"""Receive input from primitive or force Composite type to receive input (ignore = True) or iterate through properties to set values"""

	valInput, valid = None, False

	# If the object is a primitive (or forced), receive value as a primitive
	if ((isinstance(xObject, funClasses.Composite) == False) or (ignore == True)):
		print(xObject.get_symbol() + " - " + xObject.get_name() + " (" + xObject.get_unit() + "):")
		while valid != True:
			valInput = input("-> ")
			valid = xObject.set_value(valInput)

		# Break recursion
		return

	# If the object is Composite, print options
	print("## Find " + xObject.get_name() + ":")
	print("1: From value")
	i = 2
	for expression in xObject.get_expressions():
		print("{:d}".format(i) + ": " + expression.name + ": " + expression.expr_str.format(**(expression.get_symbolic())))
		i += 1

	usrInput = -1
	while usrInput not in range(1, 3):
		usrInput = int(input("-> "))
	print("## Now enter values:")

	# Input from value is selected
	if (usrInput == 1):
		# Force Composite object to receive a primitive
		process_selection(xObject, True)
	# Input by calculation was selected
	elif (usrInput == 2):
		# Iterative through the properties and set their values
		for property in xObject.get_properties():
			process_selection(property, False)

		# Try to set the Composite value
		expressionResult = xObject.try_set_value()

		if (expressionResult == -1):
			return

		# Print answer
		print("## Answer: ")
		print_answer(xObject, expressionResult)
		print("##")


def print_answer(xObject, xExprNumber):
	# Compose the left part
	left_side = xObject.get_symbol()

	expr = xObject.get_expressions()[xExprNumber]

	# Compose the middle part
	middle_expr_symb = expr.expr_str.format(**(expr.get_symbolic()))
	middle_expr_float = expr.expr_str.format(**(expr.get_values()))

	# Cmpose the right part
	right_side = "{answer:{Format}}".format(answer=xObject.get_value(), Format=DEFAULT_FLOAT_FORMAT) + " " + xObject.get_unit()

	# Print
	print(left_side + " = " + middle_expr_symb + " = " + middle_expr_float + " = " + right_side)


def main_menu(objTypes):
	"""Print the main menu while not terminated by input - 0"""

	print("# Select from the options:")
	# Instantiate and print all options
	objects = []
	i = 0
	for objType in objTypes:
		objects.append(objType())
		print(str(i+1) + ": " + objects[i].get_name())
		i += 1
	print("0: exit")

	# Receive and validate input
	usrInput = -1
	while usrInput not in range(0, i+1):
		usrInput = int(input("-> "))

	# Terminate if needed
	if (usrInput == 0):
		return
	else:
		usrInput -= 1

	# Print find options
	process_selection(objects[usrInput])

	# Repeat
	print("#\n")
	main_menu(objTypes)


# INVOKE
main_menu(rectangularFigures.AVAIL_CLASSES)
