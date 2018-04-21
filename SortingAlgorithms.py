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

	def sort(self,n=4,duplicates=True):

		if self.method == 'alphabetical':

			array = self.load_file_to_array(duplicates)

			# Store the time where all begin
			start_time = time.time()

			# Sort this array
			self.sort_array(array)

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
			self.sort_array(occurrences)

			# Calculate the time it took to sort
			self.execution_time = time.time()-start_time

			# Print all words sorted in the screen
			self.print_words(occurrences)

			# And it's execution time
			print('Execution Time (Seconds): ' + str(self.execution_time))

class InsertionSort(AbstractSortClass):

	# Sort an array using Insertion Sort
	def sort_array(self, array,n=4):
		# Loop through the entire array
		for current_foward in range( 1, len(array) ):
			
			# Go on each element before the current
			current_backwards = current_foward

			# Verify if it's a number or a word
			if type(array[current_foward]) is not int:

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
			else:

				# Check which number is smaller first 
				numberA = array[current_foward]

				# Go on each element before the current
				current_backwards = current_foward-1

				# Check which occurrence number comes first in decreasing order
				while current_backwards >=0 and numberA > array[current_backwards] :

					# Move to the right
					array[current_backwards+1] = array[current_backwards]

					# Go one step to the left
					current_backwards -= 1
				
				# Swap the numbers
				array[current_backwards+1] = numberA

class HeapSort(AbstractSortClass):

	def build_max_heap(self, array,array_size):
		for i in range(array_size, -1, -1):
			self.heapify(array, array_size, i)

	def heapify(self, array, array_size, i, alphabetical=True):
		# Supose that the root is the largest (We check this later)
		largest = i  
		left_index = 2 * i + 1     
		right_index = 2 * i + 2     
	 
		# Check if we're inside the array boundery
		if left_index < array_size or right_index < array_size:

			# Check if it's an integer or a word
			if type(array[i]) is not int:

				# See if left child of root exists and is greater than it's parent
				if left_index < array_size and utilities.this_word_comes_first_than_that(array[left_index],array[i]):
					largest = left_index
			 
				# See if right child of root exists and is greater than it's parent
				if right_index < array_size and utilities.this_word_comes_first_than_that(array[right_index],array[largest]):
					largest = right_index
			else:

				# See if left child of root exists and is smaller than it's parent
				if left_index < array_size and array[i] > array[left_index]:
					largest = left_index
				
				# See if right child of root exists and is smaller than it's parent
				if right_index < array_size and array[largest] > array[right_index]:
					largest = right_index
	 
		# Change root, if needed
		if largest != i:

			# Swap items
			array[i],array[largest] = array[largest],array[i]  
			
		    # Heapify the parent, until it's no longer required.
			self.heapify(array, array_size, largest)
	 
	# The main function to sort an array of given size
	def sort_array(self, array):
		array_size = len(array)

		# Build a maxheap.
		self.build_max_heap(array,array_size)
	 
		# One by one extract elements
		for i in range(array_size-1, 0, -1):
			array[i], array[0] = array[0], array[i]   # swap
			self.heapify(array, i, 0)

class ShellSort(AbstractSortClass):

	def sort_array(self, array):
		size=len(array)-1
		gap=1
		
		# Start gap with a size greater then array size
		while gap < size:
			gap=(gap*3)+1
		while gap > 1:
			gap /= 3

			for i in range(int(gap), size):
				value = array[i];
				j = i
				# Verify if it's a number or a word
				if type(array[i]) is not int:
					#Percorre a array nas posiÃ§Ãµes i e j, na distÃ¢ncia h atÃ© o final do vetor
					while j >= gap and utilities.this_word_comes_first_than_that(array[int(j-gap)], value):
						array[j] = array[int(j - gap)]
						j = int(j - gap)
	                    #Atualiza o valor de h             
					array[j] = value
				else:
					#Percorre a array nas posiÃ§Ãµes i e j, na distÃ¢ncia h atÃ© o final do vetor
					while j >= gap and value > array[int(j-gap)]:
						array[j] = array[int(j - gap)]
						j = int(j - gap)
	                    #Atualiza o valor de h             
					array[j] = value
		return array
