# -*- coding: utf-8 -*-
#!/usr/bin/python
import utilities,time

class AbstractSortClass():
	method = ''
	file = ''
	execution_time = -1

	def print_words(self,array):
		for word in array:
			print(word)

	def load_file_to_dictionary(self, duplicates=True):
		# Get all words and store them in a dictionary | Key = word, Value = occurrences
		dictionary = utilities.convert_file_to_dictionary(self.file)

		return dictionary

	def load_file_to_array(self, duplicates=True):
		# Get all words and store them in a dictionary | Key = word, Value = occurrences
		dictionary = utilities.convert_file_to_dictionary(self.file)

		# Get all words and put them in an unsorted array
		array = []
		if duplicates:

			# Store all words and theirs duplicates
			for key,values in dictionary.items():
				for i in range(values):
					array.append(key)			
		else:

			# Store all words whithout duplicates
			array = list(dictionary.keys())

		return array

class InsertionSort(AbstractSortClass):

	def sort(self,n=4,duplicates=True):

		if self.method == 'alphabetical':

			array = self.load_file_to_array(duplicates)

			# Store the time where all begin
			start_time = time.time()

			# Sort this array
			self.sort_alphabetical(array)

			# Calculate the time it took to sort
			self.execution_time = time.time()-start_time

			# Print all words sorted in the screen
			self.print_words(array)

			# And it's execution time
			print('Execution Time (Seconds): ' + str(self.execution_time))


		else:

			# Load the file in an array
			array = self.load_file_to_array(duplicates)

			# Load the file in a dictionary
			dictionary = self.load_file_to_dictionary()

			occurrences = []
			# For each word, store it's occurrence value
			for word in array:
				occurrences.append(dictionary[word])

			# Store the time where all begin
			start_time = time.time()

			# Sort this occurrence array
			self.sort_occurrences(occurrences)

			# Calculate the time it took to sort
			self.execution_time = time.time()-start_time

			# Print all words sorted in the screen
			self.print_words(occurrences)

			# And it's execution time
			print('Execution Time (Seconds): ' + str(self.execution_time))

	def sort_occurrences(self, arr):

		# Loop through the entire array
		for current_foward in range( 1, len(arr) ):

			numberA = arr[current_foward]

			# Go on each element before the current
			current_backwards = current_foward-1

			# Check which occurrence number comes first in decreasing order
			while current_backwards >=0 and numberA < arr[current_backwards] :

					# Move to the right
					arr[current_backwards+1] = arr[current_backwards]

					# Go one step to the left
					current_backwards -= 1
			
			# Swap the numbers
			arr[current_backwards+1] = numberA

	# Sort an array using Selection Sort
	def sort_alphabetical(self, array,n=4):
		
		# Loop through the entire array
		for current_foward in range( 1, len(array) ):
			
			# Go on each element before the current
			current_backwards = current_foward

			# Check which word comes first in alphabetic order

			this = array[current_backwards-1]
			that = array[current_backwards]

			# Do it whithout going out of the array boundery
			while current_backwards > 0 and utilities.this_word_comes_first_than_that(this,that,n=n):
					
					# Swap the words

					i = current_backwards
					j = (current_backwards - 1)

					array[i],array[j] = array[j],array[i]

					# Update their indexes to go even futher in the array
					current_backwards -= 1

					this = array[current_backwards-1]
					that = array[current_backwards]

			


class HeapSort(AbstractSortClass):

	def sort(self,n=4,duplicates=True):

		if self.method == 'alphabetical':

			array = self.load_file_to_array(duplicates)

			# Store the time where all begin
			start_time = time.time()

			# Sort this array
			self.sort_alphabetical(array)

			# Calculate the time it took to sort
			self.execution_time = time.time()-start_time

			# Print all words sorted in the screen
			self.print_words(array)

			# And it's execution time
			print('Execution Time (Seconds): ' + str(self.execution_time))


		else:

			# Load the file in an array
			array = self.load_file_to_array(duplicates)

			# Load the file in a dictionary
			dictionary = self.load_file_to_dictionary()

			occurrences = []
			# For each word, store it's occurrence value
			for word in array:
				occurrences.append(dictionary[word])

			# Store the time where all begin
			start_time = time.time()

			# Sort this occurrence array
			self.sort_occurrences(occurrences)

			# Calculate the time it took to sort
			self.execution_time = time.time()-start_time

			# Print all words sorted in the screen
			self.print_words(occurrences)

			# And it's execution time
			print('Execution Time (Seconds): ' + str(self.execution_time))

	def heapify(self, arr, n, i):
	    largest = i  # Initialize largest as root
	    l = 2 * i + 1     # left = 2*i + 1
	    r = 2 * i + 2     # right = 2*i + 2
	 
	    # See if left child of root exists and is
	    # greater than root
	    if l < n and arr[i] < arr[l]:
	        largest = l
	 
	    # See if right child of root exists and is
	    # greater than root
	    if r < n and arr[largest] < arr[r]:
	        largest = r
	 
	    # Change root, if needed
	    if largest != i:
	        arr[i],arr[largest] = arr[largest],arr[i]  # swap
	 
	        # Heapify the root.
	        self.heapify(arr, n, largest)
	 
	# The main function to sort an array of given size
	def sort_occurrences(self,arr):
	    n = len(arr)
	 
	    # Build a maxheap.
	    for i in range(n, -1, -1):
	        self.heapify(arr, n, i)
	 
	    # One by one extract elements
	    for i in range(n-1, 0, -1):
	        arr[i], arr[0] = arr[0], arr[i]   # swap
	        self.heapify(arr, i, 0)

	def sort_alphabetical(self, array, n=4):

		# Build the Max Heap (Every child must be lesser than it's parent)
		self.build_max_heap(array)

		# Goes from the (last-1) sorted element to the first element of the array
		for i in range(len(array),-1,-1):

			# Swap the first element and the last
			array[0],array[-1] = array[-1],array[0]

			# Assume that part of the tree is already sorted, and and sort only one node
			self.heapfy(array, i, n=n)

	def build_max_heap(self, array):
		for i in range( int(len(array)) , -1 , -1):
			self.heapfy(array, i)

	def heapfy(self, array, i, n=4):
		largest = i
		left_index = 2*i
		right_index = 2*i+1

		# See if left child of root exists and is greater than it's parent
		if left_index < len(array) and utilities.this_word_comes_first_than_that(array[i],array[left_index],n=n) :
		    largest = left_index

		# See if right child of root exists and is greater than it's parent
		if right_index < len(array) and utilities.this_word_comes_first_than_that(array[largest],array[right_index], n=n) :
		    largest = right_index

		# Change root, if needed
		if largest != i:
			# Swap
		    array[i],array[largest] = array[largest],array[i]

		    # Heapify the parent, until it's no longer required.
		    self.heapfy(array, largest)