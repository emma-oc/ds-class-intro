# exercise 5
'''
1. write a Python program to find those numbers
which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
'''

# code up your solution here
for i in range(1500,2700):
	if i%7==0 and i%5==0:
		print(i)

'''
2. Write a Python program to count the number of even and odd numbers from a series of numbers.
'''
num_list = [1,2,3,4,5,6,3,4,1,12,4,6,745,34352,123,6,5,3,3,432,3.1415,5.23]
odd = []
even = []
other = []

for i in num_list:
    if i%2==1:
        odd.append(i)
    elif i%2==0:
        even.append(i)
    else:
        other.append(i)

num_list2 = {'odd':odd, 'even':even, 'other':other}
print(num_list2)

odd1=0
even1=0

for i in num_list:
    if i%2==1:
        odd1+=1
    elif i%2==0:
        even1+=1

print(odd1)
print(even1)

'''how to use comprehensions to do this'''

# example: numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# output:
# >>> Number of even numbers : 4
# >>> Number of odd numbers : 5

# code up your solution here



'''
3. Write a Python program which iterates the integers from 0 to 50.
-For multiples of three print "Fizz" instead of the number
-For the multiples of five print "Buzz".
-For numbers which are multiples of both three and five print "FizzBuzz".
'''

for i in range(0,51):
    if i%5==0 and i%3==0 and i!=0:
        print('FizzBuzz')
    elif i%3==0 and i!=0:
        print('Fizz')
    elif i%5==0 and i!=0:
        print('Buzz')
    else:
        print(i)
# Expected Output :
# >>> fizzbuzz
# >>> 1
# >>> 2
# >>> fizz
# >>> 4
# >>> buzz
# >>> ...

# code up your solution here




'''
4. Given a list iterate it and display numbers which are
divisible by 5 and if you find number greater than 150 stop the loop iteration
'''
list111 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
for i in list111:
	if i>150:
		break
	elif i%5==0:
		print(i)


# examples: list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
# output:
# >>> 15
# >>> 55
# >>> 75
# >>> 150

# code up your solution here



'''
5. Pick one of the questions above and use range() for a different solution
write a Python program to find those numbers
which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
'''

for i in range(1500,2700):
	if i%7==0 and i%5==0:
		print(i)

# code up your solution here



'''
6. Pick one of the question above and use comprehension for a different solution

Write a Python program to count the number of even and odd numbers from a series of numbers.

'''

num_list = [1,2,3,4,5,6,3,4,1,12,4,6,745,34352,123,6,5,3,3,432,3.1415,5.23]
list_odd = [x for x in num_list if x%2 == 1]
print(len(list_odd))
list_even = [x for x in num_list if x%2 == 0]
print(len(list_even))

'''
7. Pcik one of the questions above and use while loop for a different solution
write a Python program to find those numbers
which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
'''
i = 1500
while i<=2700:
    i+=1
    if not (i%5==0 and i%7==0):
        continue
    print(i)

# code up your solution here



#Exercise 6

'''
1.def calculation(a, b):
''' '''
	Write a function calculation() such that it can accept two variables
	and calculate the addition and subtraction of it.
	It must return both addition and subtraction in a single return call

	Expected output:
	res = calculation(40, 10)
	print(res)
	>>> (50, 30)

	Arguments:
	a: first number
	b: second number

	Returns:
	sum: sum of two numbers
	diff: difference of two numbers
'''

def calculation(a, b):
    return (a+b,a-b)

print(calculation(10,2))
print(calculation(40,10))



'''
2.def triangle_lambda():
''' '''
	Return a lambda object that takes in a base and height of triangle
	and computes the area.

	Arguments:
	None

	Returns:
	lambda_triangle_area: the lambda
'''

triangle_lambda = lambda x,y: x*y*0.5
print(triangle_lambda(3,4))
print(type(triangle_lambda))


''''
3.def sort_words(hyphen_str):
''' '''
	Write a Python program that accepts a hyphen-separated sequence of words
	as input, and prints the words in a hyphen-separated sequence after
	sorting them alphabetically.

	Expected output:
	sort_words('green-red-yellow-black-white')
	>>> 'black-green-red-white-yellow'

	Arguments:
	hyphen_str: input string separated by hyphen

	Returns:
	sorted_str: string in a hyphen-separated sequence after
	sorting them alphabetically
'''

def sort_words(hypehn_string):
    hypehn_string=[n for n in hypehn_string.split('-')]
    hypehn_string.sort()
    return("The alphabetically sorted words are:" + '-'.join(hypehn_string))

sort_words('green-red-yellow-black-white')

'''
4.def perfect_number():
''''''
	Write a Python function to check whether a number is perfect or not.

	A perfect number is a positive integer that is equal to the sum of
	its proper positive divisors. Equivalently, a perfect number is a number
	that is half the sum of all of its positive divisors (including itself).

	Example: 6 is a perfect number as 1+2+3=6. Also by the second definition,
	(1+2+3+6)/2=6. Next perfect number is 28=1+2+4+7+14. Next two perfect
	numbers are 496 and 8128.

	Argument:
	number: number to check

	Returns:
	perfect: boolean, True if number is perfect
''''

def perfect_number(a):
    sum1=0
    for i in range(1, a):
        if(a%i==0):
            sum1=sum1+i
    if sum1==a:
        return True
    else:
        return False

perfect_number(8128)


if __name__ == '__main__':
	pass


''''
Edit this file to complete Exercise 7
'''

import csv
import json
import os
import os.path
from os import path
from pathlib import Path
# import the modules you need here

'''
1.def check_path(path):
	''''''
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
		''''
def check_path(xyz):
    list123=[]
    if path.exists(xyz) == True:
        list123.append(path.isabs(xyz))
        list123.append(path.isfile(xyz))
        list123.append(path.isdir(xyz))
    print(str(path.exists(xyz)) + ',' + str (list123))

	check_path('/Users/sun/Desktop/ds-class-intro')

	'''
	Example:
	check_path('some/path/of/a/directory')
	# if it exists
	>>> True, [False, True, False]

	# if doesn't exist
	>>> False, []
	'''



'''       ****************************Question Mark***********************************
2.def read_csv(file):
	''''''
	reads in a csv file then return the total number of lines in it

	Arguments:
	file: path to the file to read

	Returns:
	Number of rows in the input file

	Example:
	read_csv('AMZN.csv')
	>>> 14
	'''

'''There is something wrong with this question, but I cannot figure out	'''
def read_csv1(file):
    open(file,'r')
    reader = csv.reader(file)
    num_line = len(list(reader))
    print(num_line)
read_csv1('AMZN.csv')

def read_csv2(file):
    open(file,'r')
    num_line=0
    reader = csv.reader(file)
    for row in reader:
        num_line+=1
    print(num_line)
read_csv2('AMZN.csv')

def read_csv3(file):
    open(file,'r')
    reader = csv.reader(file)
    row_count = sum(1 for row in reader)
    print(row_count)
read_csv2('AMZN.csv')

'''
3.def write_csv(data_list, output_file):
	''' '''
	write out a csv file for the data list (structed as list of list),
	where each item in the data_list is a row in output file, and
	every element in the sublist is separated by comma

	Arguments:
	data_list: input data list, each elemet is a list representing
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
	''''
''''
data_list = [(1,2,3,4), (5,6,7,8), (9,10,11,12)]
def write_csv(data_input,file_output):
	with open('example.csv', 'w', newline='') as file:
    	writer = csv.writer(file)
    	writer.writerow([input('row 1 column 1:'), input('row 1 column 2:'), input('row 1 column 3:'), input('row 1 column 4:')]
		writer.writerow([input('row 2 column 1:'), input('row 2 column 2:'), input('row 2 column 3:'), input('row 2 column 4:')])
		writer.writerow([input('row 3 column 1:'), input('row 3 column 2:'), input('row 3 column 3:'), input('row 3 column 4:')])
'''

'''need a better solution'''
def write_csv(data_input,file_output):
	with open(file_output, 'w', newline='') as file:
		writer = csv.writer(file)
		writer.writerow(data_list[0])
		writer.writerow(data_list[1])
		writer.writerow(data_list[2])

data_list = [(1,2,3,4), (5,6,7,8), (9,10,11,12)]
write_csv(data_list, 'example.csv')
	# code up your solution here

''''
4.def read_json(file):
	''''''
	reads a JSON file and return its contents as a dictionary

	Arguments:
	file: path to the file to read

	Returns:
	A dictionary containing JSON contents

	Example:
	read_json('some.json')
	>>> [{'name': 'emma', 'skill': {'coding1': 'python', 'coding2': 'r'}, 'role': 0}]
	''''

def read_json(file):
    with open(file) as f:
        js = json.load(f)
        print(js)

read_json('some.json')

	# code up you solution here


if __name__=="__main__":
	pass
