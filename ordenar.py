import sys
import algorithms

filename = '1 primeira entrada.txt' 

sorting_algorithm_choosen = algorithms.InsertSort()
sorting_algorithm_choosen.sort(filename)


algorithms.convert_file_to_array(filename)
