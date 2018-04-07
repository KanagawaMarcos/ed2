import os

def convert_file_to_array(filename):
	array = []

	with open(filename) as f:
			for line in f:
				array += line.split()

	return array
