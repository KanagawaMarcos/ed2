import utilities

class SelectionSort():

	# Sort an array using Selection Sort
	def sort_array(self, array):

		# Loop through the entire array
		for cur_main_index in range( ( len(array) - 1 ) ):
			
			# Go on each element after the current
			for possible_swap_index in range( (cur_main_index + 1) , len(array)):

				# Check which word comes first in alphabetic order

				this = array[cur_main_index]
				that = array[possible_swap_index]

				if utilities.this_word_comes_first_than_that(this, that):

					# Swap the words

					i = cur_main_index
					j = possible_swap_index

					array[i],array[j] = array[j],array[i]

	