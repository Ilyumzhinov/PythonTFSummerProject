import funClasses
from funClasses import DEFAULT_NEGATIVE_VALUE, DEFAULT_NAME


# CLASSES
class RectanglePerimeter(funClasses.Perimeter):
	"""Perimeter implementation for a rectangle figure"""

	def __init__(self):
		"""Initialise length and width and add them to properties"""
		super(funClasses.Perimeter, self).__init__()

		# Set defaults
		self.set_name("Perimeter of Rectangle")

		# Initialise properties
		__l = funClasses.Length()
		__w = funClasses.Length()
		__l.set_name("Length")
		__w.set_name("Width")

		# Add to Properties
		self.add_property(__l)
		self.add_property(__w)

	def assign_properties(self, *args):
		"""Validate and set length and width"""

		if (len(args) == 2):
			# Validate
			if ((self.get_properties()[0].validate_value(args[0]) == False) 
				or (self.get_properties()[1].validate_value(args[1]) == False)):
				return False
			
			# Set properties
			self.get_properties()[0].set_value(args[0])
			self.get_properties()[1].set_value(args[1])

			# Try to calculate a value
			return self.set_value(True, self.calculate_rect_perimeter(self.properties[0], self.properties[1]))
		else:
			return False

	def calculate_rect_perimeter(self, _l, _w):
		"""Standard formula for calculating a rectangle's perimeter"""
		l = _l.get_value()
		w = _w.get_value()

		return 2 * (l + w)


class RectangleArea(funClasses.Area):
	def __init__(self):
		"""Initialise length and width and add them to properties"""
		super(RectangleArea, self).__init__()

		# Set defaults
		self.set_name("Area of Rectangle")

		# Initialise properties
		__l = funClasses.Length()
		__w = funClasses.Length()
		__l.set_name("Length")
		__w.set_name("Width")

		# Add to Properties
		self.add_property(__l)
		self.add_property(__w)

	def assign_properties(self, *args):
		"""Validate and set length and width"""

		if (len(args) == 2):
			# Validate
			if ((self.get_properties()[0].validate_value(args[0]) == False) 
				or (self.get_properties()[1].validate_value(args[1]) == False)):
				return False
			
			# Set properties
			self.get_properties()[0].set_value(args[0])
			self.get_properties()[1].set_value(args[1])

			# Try to calculate a value
			return self.set_value(True, self.calculate_rect_area(self.properties[0], self.properties[1]))
		else:
			return False

	def calculate_rect_area(self, _l, _w):
		"""Standard formula for calculating a rectangle's area"""
		l = _l.get_value()
		w = _w.get_value()

		return l * w

class SquarePerimeter(RectanglePerimeter):
	def __init__(self):
		"""Initialise using the rectangle's class but remove the width (b) property"""
		super(SquarePerimeter, self).__init__()
		self.remove_property(self.get_properties()[1])

		# Set defaults
		self.set_name("Perimeter of Square")

	def assign_properties(self, *args):
		"""Validate and set length (a)"""

		if (len(args) == 1):
			# Validate
			if (self.get_properties()[0].validate_value(args[0]) == False):
				return False
			
			# Set property
			self.get_properties()[0].set_value(args[0])

			# Try to calculate a value
			return self.set_value(True, self.calculate_rect_perimeter(self.properties[0], self.properties[0]))
		else:
			return False


class SquareArea(RectangleArea):
	def __init__(self):
		"""Initialise using the rectangle's class but remove the width (b) property"""
		super(SquareArea, self).__init__()
		self.remove_property(self.get_properties()[1])

		# Set defaults
		self.set_name("Area of Square")

	def assign_properties(self, *args):
		"""Validate and set length and width"""

		if (len(args) == 1):
			# Validate
			if (self.get_properties()[0].validate_value(args[0]) == False):
				return False
			
			# Set properties
			self.get_properties()[0].set_value(args[0])

			# Try to calculate a value
			return self.set_value(True, self.calculate_rect_area(self.properties[0], self.properties[0]))
		else:
			return False


# GLOBAL
# List of available classes as types
AVAIL_CLASSES = [
RectanglePerimeter,
RectangleArea,
SquarePerimeter,
SquareArea
]
