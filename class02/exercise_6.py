'''
Edit this file to complete Exercise 6
'''

def calculation(a, b):
	'''
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

	# code up your solution here
	summation = a + b
	diff = a - b
	return summation, diff



def triangle_lambda():
	'''
	Return a lambda object that takes in a base and height of triangle
	and computes the area.

	Arguments:
	None

	Returns:
	lambda_triangle_area: the lambda
	'''
	return lambda base, height: .5 * base * height




def sort_words(hyphen_str):
	'''
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

	# code up your solution here
	words = hyphen_str.split('-')
	words.sort()
	hyphen = '-'
	sorted_hyphen_str = hyphen.join(words)
	return sorted_hyphen_str




def perfect_number(n):
	'''
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
	'''

	# code up your answer here
	if n < 1:
		return 'Invalid Number'
	if n == 1:
		return True
	list2 = [1]
	for i in range(2, n // 2 + 1):
		if n % i == 0:
			list2.append(i)
	return n == sum(list2)



if __name__ == '__main__':
	pass