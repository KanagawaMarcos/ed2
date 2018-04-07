import sys
import algorithms

filename = '1 primeira entrada.txt' 

sorting_algorithm_choosen = algorithms.SelectionSort()

array = algorithms.convert_file_to_array(filename)

sorting_algorithm_choosen.sort(array)

print('----------------------')
print(array)