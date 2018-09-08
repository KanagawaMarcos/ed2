# -*- coding: utf-8 -*-
#!/usr/bin/python

import os

from removedor_de_acentos import remover_acentos

def convert_file_to_array(filename, type_of_input='integer'):
	array = []

	# Open the file an separete each word in an array element
	with open(filename) as file:
		for line in file:
			array += line.split()

	if type_of_input == 'integer':
		array = list(map(lambda current : int(current), array))
	return array

def convert_file_to_dictionary(filename, type_of_input='integer'):

	array = []

	array = convert_file_to_array(filename)

	# Key = Word | Value = Occurrence
	dictionary = {}
	for key in array:
		if key in dictionary:
			dictionary[key] += 1
		else:
			dictionary[key] = 1


	return dictionary


def this_number_comes_first_than_that(this, that):
	return this < that

# Check which word comes first in alphabetical order
def this_word_comes_first_than_that(this, that, minimum_word_size=4, n=4):

	# If both words has the minimum amout of letters or more

	if(len(this) >= minimum_word_size and len(that) >= minimum_word_size):

		# Which word has the smaller size?

		smaller_size = len(this)
		if len(that) < smaller_size:
			smaller_size = len(that)

		if n < smaller_size:
			smaller_size = n

		# Iterate until a given N or the smallest word size
		for current_letter in range(smaller_size):

			# Return the True if "this" comes first, otherwise return False

			if remover_acentos(this)[current_letter].lower() > remover_acentos(that)[current_letter].lower():
				return True
			elif remover_acentos(this)[current_letter].lower() < remover_acentos(that)[current_letter].lower():
				return False
