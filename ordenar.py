# -*- coding: utf-8 -*-
import utilities
from SelectionSort import SelectionSort
from InsertionSort import InsertionSort
from HeapSort import HeapSort



filename = '1 primeira entrada.txt'
#filename = 'deleteme.teste.txt'

sorting_algorithm_choosen = SelectionSort()
#sorting_algorithm_choosen = InsertionSort()
#sorting_algorithm_choosen = HeapSort()

dictionary = utilities.convert_file_to_dictionary(filename)



#array = utilities.convert_file_to_array(filename)
array = dictionary.keys()


sorting_algorithm_choosen.sort_array(array)

print('----------------------')
print(array)

#i = 1
#for key in dictionary:
#	i+=1
#	print(key + ' | ocorrências:'+ str(dictionary[key]))

