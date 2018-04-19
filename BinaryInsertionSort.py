import utilities

class BinaryInsertionSort():

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

			

	# Returns the index where this searched item is
	def binary_search(self, array, left, right, value):
		# ???????
		if left == right:
			if array[left] > value:
				return left+1
			else:
				return left
		# ????????
		if left > right:
			return left

		middle = (left + right)//2

		# If it's smaller, the value is in the left subarray
		if array[middle] < value:
			return self.binary_search(array, left, middle-1,value)

		# If it's greater, then this value must be at the right subarray
		elif array[middle] > value:
			return self.binary_search(array, middle+1, right,value)

		# If we ge here, so this element is not in this array, return where it stopped
		else:
			return middle