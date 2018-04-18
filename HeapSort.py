import utilities

class HeapSort():

	def sort_array(self, array):

		# Build the Max Heap (Every child must be lesser than it's parent)
		self.build_max_heap(array)

		# Goes from the (last-1) sorted element to the first element of the array
		for i in range(len(array),-1,-1):

			# Swap the first element and the last
			array[0],array[-1] = array[-1],array[0]

			# Assume that part of the tree is already sorted, and and sort only one node
			self.heapfy(array, i)

	def build_max_heap(self, array):
		for i in range( int(len(array)) , -1 , -1):
			self.heapfy(array, i)

	def heapfy(self, array, i):
		largest = i
		left_index = 2*i
		right_index = 2*i+1

		# See if left child of root exists and is greater than it's parent
		if left_index < len(array) and utilities.this_word_comes_first_than_that(array[i],array[left_index]) :
		    largest = left_index

		# See if right child of root exists and is greater than it's parent
		if right_index < len(array) and utilities.this_word_comes_first_than_that(array[largest],array[right_index]) :
		    largest = right_index

		# Change root, if needed
		if largest != i:
			# Swap
		    array[i],array[largest] = array[largest],array[i]

		    # Heapify the parent, until it's no longer required.
		    self.heapfy(array, largest)
