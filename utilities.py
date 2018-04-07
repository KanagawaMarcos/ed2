import os

def convert_file_to_array(filename):
	array = []

	with open(filename) as file:
			for line in file:
				array += line.split()

	return array
