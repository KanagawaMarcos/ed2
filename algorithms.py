import os

class InsertSort():

	def sort(self ,filename ):
		with open(filename) as f:
			for line in f:
				for word in line:
					print(word)


class SelectionSort():

	def sort(self, filename):
		pass

	def this_comes_first_than_that(self, this, that):
		pass