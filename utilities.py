import os

def convert_file_to_dictionary(filename):
	array = []

	with open(filename) as file:
		for line in file:
			array += line.split()

	# Key = Word | Value = Occurrence
	dictionary = {}
	for word in array:
		if word in dictionary:
			dictionary[word] += 1
		else:
			dictionary[word] = 1


	return dictionary
