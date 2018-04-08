import utilities
from SelectionSort import SelectionSort
from InsertionSort import InsertionSort
from HeapSort import HeapSort




filename = '1 primeira entrada.txt' 
#filename = 'deleteme.teste.txt' 

sorting_algorithm_choosen = SelectionSort()
sorting_algorithm_choosen = InsertionSort()
sorting_algorithm_choosen = HeapSort()




array = utilities.convert_file_to_array(filename)
#print(array)

sorting_algorithm_choosen.sort_array(array)

print('----------------------')
print(array)

#dictionary = utilities.convert_file_to_dictionary(filename)