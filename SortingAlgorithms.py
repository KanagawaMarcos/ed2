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

	# Returns the index where this searched item is
	def binary_search(self, array, left, right, value):
		# ???????
		if left == right:
			if type(array[left]) is not int:
				if utilities.this_word_comes_first_than_that(array[left], value):
					return left+1
				else:
					return left
			else:
				if array[left] > value:
					return left+1
				else:
					return left
		# ????????
		if left > right:
			return left

		middle = (left + right)//2

		# Verify if it's a number or a word
		if type(array[middle]) is not int:

			# If it's smaller, the value is in the left subarray
			if utilities.this_word_comes_first_than_that(array[middle], value):
				return self.binary_search(array, left, middle-1,value)

			# If it's greater, then this value must be at the right subarray
			elif utilities.this_word_comes_first_than_that(value,  array[middle]):
				return self.binary_search(array, middle+1, right,value)

			# If we ge here, so this element is not in this array, return where it stopped
			else:
				return middle
		else:
			# If it's smaller, the value is in the left subarray
			if array[middle] < value:
				return self.binary_search(array, left, middle-1,value)

			# If it's greater, then this value must be at the right subarray
			elif array[middle] > value:
				return self.binary_search(array, middle+1, right,value)

			# If we ge here, so this element is not in this array, return where it stopped
			else:
				return middle
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

class SelectionSort(AbstractSortClass):

	# Sort an array using Selection Sort
	def sort_array(self, array):

		# Loop through the entire array
		for cur_main_index in range( ( len(array) - 1 ) ):
			
			# Go on each element after the current
			for possible_swap_index in range( (cur_main_index + 1) , len(array)):

				# Verify if it's a number or a word
				if type(array[possible_swap_index]) is not int:
					# Check which word comes first in alphabetic order

					this = array[cur_main_index]
					that = array[possible_swap_index]

					if utilities.this_word_comes_first_than_that(this, that):

						# Swap the words

						i = cur_main_index
						j = possible_swap_index

						array[i],array[j] = array[j],array[i]
				else:
					# Check which number comes first in alphabetic order

					numberA = array[cur_main_index]
					numberB = array[possible_swap_index]

					if numberA < numberB:

						# Swap the words

						i = cur_main_index
						j = possible_swap_index

						array[i],array[j] = array[j],array[i]

class BinaryInsertionSort(AbstractSortClass):

	# Sort an array using Selection Sort
	def sort_array(self, array):
		
		# Loop through the entire array
		for current_foward in range( 1, len(array) ):
			
			
			# Find where insert the current word
			index_to_insert = self.binary_search(array,0, current_foward-1,array[current_foward])

			# Save a copy from the element to insert
			element = array[current_foward]

			# Go on each element before the current			
			for current_backwards in range(current_foward-1,index_to_insert-1,-1):
				array[current_backwards+1] = array[current_backwards]

			# Insert the element
			array[index_to_insert] = element

class TimSort(AbstractSortClass):
	def insertion_sort(self, array):
		l = len(array)
		for index in range(1, l):
			value = array[index]
			pos = self.binary_search(array, value, 0, index - 1)
			array = array[:pos] + [value] + array[pos:index] + array[index+1:]
		return array
	
	# Takes two sorted lists and returns a single sorted list by comparing the	elements one at a time.
	def merge(self,left, right):

		# Check if any of it's array exist
		if not left:
			return right
		if not right:
			return left

		# Verify if it's a number or a word
		if type(left[0]) is not int:

			# Do a default merge sort 
			if utilities.this_word_comes_first_than_that(left[0], right[0]):
				return [left[0]] + self.merge(left[1:], right)			
		else:
			# Do a default merge sort 
			if left[0] < right[0]:
				return [left[0]] + self.merge(left[1:], right)
		return [right[0]] + self.merge(left, right[1:])

	def sort_array(self,array):

		runs, sorted_runs = [], []
		l = len(array)
		new_run = [array[0]]

		for i in range(1, l):
			if i == l-1:
				new_run.append(array[i])
				runs.append(new_run)
				break
			# Verify if it's a number or a word
			if type(array[i]) is not int:
				if utilities.this_word_comes_first_than_that(array[i], array[i-1]):
					if not new_run:
						runs.append([array[i]])
						new_run.append(array[i])
					else:
						runs.append(new_run)
						new_run = []
				else:
					new_run.append(array[i])
			else:
				if array[i] < array[i-1]:
					if not new_run:
						runs.append([array[i]])
						new_run.append(array[i])
					else:
						runs.append(new_run)
						new_run = []
				else:
					new_run.append(array[i])

		insertion_sort = InsertionSort()
		for each in runs:
			sorted_runs.append(self.insertion_sort(each))

		sorted_array = []
		for run in sorted_runs:
			sorted_array = self.merge(sorted_array, run)

class QuickSort(AbstractSortClass):
	def sort_array(self,array):
		end=len(array)
		self.QuickSort(array,0,end)
		return array
	def particiona(self, array, begin, end):
		i=begin
		j=end-1
		meio = int((i+j)/2)
		pivo=array[meio]
		#Troca o pivÃ´ com o primeiro elemento
		array[i],array[meio] = array[meio],array[i]
		i=+1
		loop_j=0
		while j>i:
			loop_j=0
			# Verify if it's a number or a word
			if type(array[i]) is not int:
				#Testa se a palavra em left vem antes da palavra em pivÃ´
				if array[i] < pivo:
					i=i+1
				else:
					while loop_j==0:
						#Atribui a variavÃ©l right a palavra em array[j]
	                                                                        
						#Testa se a palavra no pivÃ´ vem antes da palavra em right
						if pivo < array[j]:
							j=j-1
						else:
							#Troca as palavras no array nas posiÃ§Ãµes i e j
							array[i],array[j] = array[j],array[i]
							#Movimenta as variaveis
							i=i+1
							j=j-1
							#Encerra o Loop
							loop_j=loop_j+1
			else:
				#Testa se a palavra em left vem antes da palavra em pivÃ´
				if utilities.this_word_comes_first_than_that(array[i],pivo):
					i=i+1
				else:
					while loop_j==0:
						#Atribui a variavÃ©l right a palavra em array[j]
	                                                                        
						#Testa se a palavra no pivÃ´ vem antes da palavra em right
						if utilities.this_word_comes_first_than_that(pivo,array[j]):
							j=j-1
						else:
							#Troca as palavras no array nas posiÃ§Ãµes i e j
							array[i],array[j] = array[j],array[i]
							#Movimenta as variaveis
							i=i+1
							j=j-1
							#Encerra o Loop
							loop_j=loop_j+1
		if i>j:
			#Troca as palavras no array nas posiÃ§Ãµes meio e j
			array[begin],array[j]=array[j],array[begin]
                                        
			print (array[j])
			return j
		return j                                 
	def QuickSort(self, array, begin, end):
		if 1>=end:
			return array
		elif begin < end :
			#Atribui a variavÃ©l num o valor que serÃ¡ retornado em particiona
			num=self.particiona(array, begin, end)
			#Usa a variavÃ©l num para determinar um novo fim e comeÃ§o para a funÃ§Ã£o quicksort
			self.QuickSort(array, begin, num)
			self.QuickSort(array, num+1, end)
			return array

