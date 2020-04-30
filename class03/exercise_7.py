'''
Edit this file to complete Exercise 7
'''


# import the modules you need here


def check_path(pathname):
	'''
	check if the input path exists, if it exists, return True and a
	list containing the following
		1. if this path is absolute path
		2. if this path is a directory
		3. if this path is a file
	if input path doesn't exist, return False and empty list

	Arguments:
	path: input path as a string

	Returns:
	exist_flag: True if path exist, False otherwise
	path_info_list: list containing 3 boolean varaibles for 3 checks
		performed if path exists, return empty list if path doesn't
		exist.

	Example:
	check_path('some/path/of/a/directory')
	# if it exists
	>>> True, [False, True, False]

	# if doesn't exist
	>>> False, []
	'''
	import os
	from os import path
	checklist = []
	if path.exists(pathname):
		check1 = 'True'
		checklist.append(path.isabs(pathname))
		checklist.append(path.isdir(pathname))
		checklist.append(path.isfile(pathname))
	else:
		check1 = 'False'
	print(check1, ',', checklist)


def read_csv(filepath):
	'''
	reads in a csv file then return the total number of lines in it

	Arguments:
	file: path to the file to read

	Returns:
	Number of rows in the input file

	Example:
	read_csv('AMZN.csv')
	>>> 14
	'''

	# code up your solution here
	import csv
	row_count = 0
	with open(filepath, 'r') as f:
		reader = csv.reader(f, delimiter=',')
		for row in reader:
			row_count += 1
	return row_count


def write_csv(data_list, output_file):
	'''
	write out a csv file for the data list (structed as list of list), 
	where each item in the data_list is a row in output file, and 
	every element in the sublist is separated by comma

	Arguments:
	data_list: input data list, each element is a list representing
		a row with values for each column
	file: path to save the csv file 

	Returns:
	None

	Example:
	data_list = [(1,2,3,4), (5,6,7,8), (9,10,11,12)]
	write_csv(data_list, 'example.csv')
	
	'example.csv' looks like below:
	1,2,3,4
	5,6,7,8
	9,10,11,12
	'''

	# code up your solution here
	import csv
	with open(output_file, 'w', newline='') as f:
		writer = csv.writer(f)
		for sublist in data_list:
			writer.writerow(sublist)


def read_json(file):
	'''
	reads a JSON file and return its contents as a dictionary

	Arguments:
	file: path to the file to read

	Returns:
	A dictionary containing JSON contents

	Example:
	read_json('some.json')
	>>> [{'name': 'emma', 'skill': {'coding1': 'python', 'coding2': 'r'}, 'role': 0}]
	'''


# code up you solution here
	import json
	with open(file) as f:
		js = json.load(f)
	return js


if __name__ == "__main__":
	check_path('AMZN.csv')
	print(read_csv('AMZN.csv'))
	write_csv(data_list=[(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12)], output_file='example.csv')
	print(read_json('some.json'))
	pass
