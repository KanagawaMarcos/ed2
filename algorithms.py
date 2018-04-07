import os

class InsertSort():

	def sort(self ,filename ):
		pass


class SelectionSort():

	def sort(self, array):
		pass

	def __this_comes_first_than_that(self, this, that):
		pass

def convert_file_to_array(filename):
	array = []
	with open(filename) as f:
			for line in f:
				array += line.split()
			