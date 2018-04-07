import os

class InsertSort():

	def sort(self ,filename ):
		pass


class SelectionSort():

	# Sort an array using Selection Sort
	def sort(self, array):

		# Loop through the entire array
		for cur_main_index in range( ( len(array) - 1 ) ):
			
			# Go on each element after the current
			for possible_swap_index in range( (cur_main_index + 1) , len(array)):

				# Check which word comes first in alphabetic order

				this = array[cur_main_index]
				that = array[possible_swap_index]

				if self.__this_word_comes_first_than_that(this, that):

					# Swap the words

					i = cur_main_index
					j = possible_swap_index

					array[i],array[j] = array[j],array[i]


	# Check which word comes first in alphabetical order
	def __this_word_comes_first_than_that(self, this, that, minimum_word_size=4):

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
