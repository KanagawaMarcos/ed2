import utilities
from SelectionSort import SelectionSort
from InsertionSort import InsertionSort



filename = '1 primeira entrada.txt' 
filename = 'deleteme.teste.txt' 

#sorting_algorithm_choosen = SelectionSort()
sorting_algorithm_choosen = InsertionSort()


array = utilities.convert_file_to_array(filename)
print(array)

sorting_algorithm_choosen.sort_array(array)

print('----------------------')
print(array)

#dictionary = utilities.convert_file_to_dictionary(filename)