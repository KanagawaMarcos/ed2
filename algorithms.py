import os

class InsertSort():

	def sort(self ,filename ):
		pass


class SelectionSort():

	def sort(self, array):
		pass

	def __this_comes_first_than_that(self, this, that, minimum_word_size=4):

		# If both words has the minimum amout of letters or more

		if(len(this) >= minimum_word_size and len(that) >= minimum_word_size):

			# Which one has the greater size?
			
			greater_size = len(this)
			if len(that) > greater_size:
				greater_size = len(that)

			# Return the True if "this" comes first, otherwise return False
			
			for current_letter in range(greater_size):

				if this[current_letter].lower() > that[current_letter].lower():
					return True
				elif this[current_letter].lower() < that[current_letter].lower():
					return False

def convert_file_to_array(filename):
	array = []

	with open(filename) as f:
			for line in f:
				array += line.split()

	return array
