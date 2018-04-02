import os

class InsertSort():

	def sort(self ,filename ):
		with open(filename) as f:
			for line in f:
				for word in line:
					print(word)