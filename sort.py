# -*- coding: utf-8 -*-
#!/usr/bin/python

import utilities
from SortingAlgorithms import InsertionSort,HeapSort,ShellSort
from SelectionSort import SelectionSort
from BinaryInsertionSort import BinaryInsertionSort

def how_to_use():
	print('----------------------------------------------------------------------') 
	print('Example:') 
	print('python3 sort.py -a heapsort -m alphabetical -f 1\ primeira\ entrada.txt') 

def error(name):
	print('----------------------------------------------------------------------') 
	print(name + ' is not valid!') 
	print('Usage Example:') 
	print('python3 sort.py -a heapsort -m alphabetical -f 1\ primeira\ entrada.txt') 

import argparse,sys
def menu(argv):
	# Create an argument parser
	parser = argparse.ArgumentParser()

	# Adds the arguments used in this project
	parser.add_argument('-a', '--algorithm')
	parser.add_argument('-m', '--method')
	parser.add_argument('-f', '--file')

	# Save the list of arguments to handle them
	args = parser.parse_args()

	if args.algorithm is None:
		print('You need to choose a sort algorithm!')
		print('Supported algorithms:')

		print('-InsertSort')
		print('-ShellSort')
		print('-QuickSort')
		print('-HeapSort')
		print('-BinaryInsertSort')
		print('-IntroSort')
		print('-TimSort')

		how_to_use()
		sys.exit(2)

	if args.method is None:
		print('You need to choose a method!')
		print('Supported methods:')

		print('-Alphabetical')
		print('-Occurrences')

		how_to_use()
		sys.exit(2)

	if args.method is None:
		print('You need to set a file!')
		print('Example:')
		print('-Readme.txt')

		how_to_use()
		sys.exit(2)

	return args
def create_algorithm(algorithm):

	if algorithm == 'insertionsort' or algorithm == 'insertsort':
		return InsertionSort()

	elif algorithm == 'selectionsort' or algorithm == 'selectsort':
		return SelectionSort()

	elif algorithm == 'quicksort':
		return QuickSort()

	elif algorithm == 'heapsort':
		return HeapSort()

	elif algorithm == 'shellsort':
		return ShellSort()
	
	elif algorithm == 'binaryinsertionsort' or algorithm == 'binaryinsertsort':
		return BinaryInsertSort()

	elif algorithm == 'introsort':
		return IntroSort()

	elif algorithm == 'timsort':
		return TimSort()

	else:
		error(algorithm)
		sys.exit(2)

if __name__ == "__main__":
	
	# Get user's arguments
	arguments = menu(sys.argv[1:])
	
	# Get a string for each argument
	algorithm = arguments.algorithm.lower()

	filename = arguments.file.lower()

	method = arguments.method.lower()

	# Creat a sort algorithm object 
	algorithm = create_algorithm(algorithm)
	
	# Set it's atributes and sort 
	algorithm.method = method
	algorithm.file = filename
	algorithm.sort(duplicates=False)
	## NEED TO CHECK THE METHOD IF IT'S VALID AND FILE AS WELL

"""
sorting_algorithm_choosed = BinaryInsertionSort()
#sorting_algorithm_choosen = SelectionSort()
"""