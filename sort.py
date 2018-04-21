# -*- coding: utf-8 -*-
#!/usr/bin/python

import utilities
from SelectionSort import SelectionSort
from InsertionSort import InsertionSort
from HeapSort import HeapSort
from BinaryInsertionSort import BinaryInsertionSort

def how_to_use():
	print('----------------------------------------------------------------------') 
	print('Example:') 
	print('python3 order.py -a heapsort -m alphabetical -f 1\ primeira\ entrada.txt') 

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
		print('-Binary InsertSort')
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


if __name__ == "__main__":

	menu(sys.argv[1:])
	
"""
filename = '1 primeira entrada.txt'
#filename = 'deleteme.teste.txt'

sorting_algorithm_choosen = BinaryInsertionSort()
#sorting_algorithm_choosen = SelectionSort()
#sorting_algorithm_choosen = InsertionSort()
#sorting_algorithm_choosen = HeapSort()

dictionary = utilities.convert_file_to_dictionary(filename)


#array = utilities.convert_file_to_array(filename)
array = list(dictionary.keys())

#array_occurrence = []

#for word in array:
#	array.append(dictionary[word])

sorting_algorithm_choosen.sort_array(array)


for word in array:
	print(word)
print('----------------------\n')
print('tamanho: '+str(len(array)))
"""