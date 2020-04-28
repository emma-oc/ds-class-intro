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
	def calculation(a,b):
    		sum = a + b
    		diff = a - b
    		return [sum,diff];


def triangle_lambda():
	'''
	Return a lambda object that takes in a base and height of triangle
	and computes the area.

	Arguments:
	None

	Returns:
	lambda_triangle_area: the lambda
	'''
	def triangle_lambda():
		lambda_triangle_area = lambda b,h: b*h/2
		return lambda_triangle_area;


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
	def sort_words(hyphen_str):
    		words_list = hyphen_str.split("-")
    		words_list.sort()
    		hyphen_str_sorted = '-'.join(words_list)
    		return hyphen_str_sorted
    
		sort_words('green-red-yellow-black-white')


def perfect_number():
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
	def is_prime_number(x):
    		if x >= 2:
        		for y in range(2,x):
           			 if not ( x % y ):
                			return False
   	 	else:
        		return False
    		return True;
	
	def multiplyList(myList) : 
    		result = 1
    		for x in myList: 
         		result = result * x  
    		return result;
	
	def perfect_number(num):
    		prime_divisors = [1]
    		for i in range(1, int(num / 2) + 1):
        		if num % i == 0:
            			if is_prime_number(i) == True:
                			prime_divisors.append(i)
    		if (sum(prime_divisors)+num)/2 == num and multiplyList(prime_divisors) == num:
        		return True
    		else:
        		return False
if __name__ == '__main__':
	pass
