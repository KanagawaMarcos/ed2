import utilities
from SelectionSort import SelectionSort


filename = '1 primeira entrada.txt' 
filename = 'deleteme.teste.txt' 

sorting_algorithm_choosen = SelectionSort()

dictionary = utilities.convert_file_to_dictionary(filename)

sorting_algorithm_choosen.sort(dictionary)

print('----------------------')
print(dictionary)