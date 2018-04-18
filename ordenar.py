# -*- coding: utf-8 -*-
import utilities
from SelectionSort import SelectionSort
from InsertionSort import InsertionSort
from HeapSort import HeapSort
from BinaryInsertionSort import BinaryInsertionSort




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
