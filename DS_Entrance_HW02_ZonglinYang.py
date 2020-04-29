# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 09:45:48 2020

@author: Zonglin
"""
# Exerciese 05
# 1. Write a Python program to find those numbers which are divisible by 7 and 
# multiple of 5, between 1500 and 2700 (both included).

def question01():
    numList = []
    for i in range(1500, 2701):
        if i % 7 == 0 and i % 5 == 0:
            numList.append(i)
    print (numList)

question01()


# 2. Write a Python program to count the number of even and odd numbers from a 
# series of numbers.
# Sample: numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# Expected Output :
# Number of even numbers : 5
# Number of odd numbers : 4 [wrong example .................]

def question02(num_series):
    even_count = odd_count = 0
    for i in num_series:
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print ('Number of even number : ', even_count)
    print ('Number of odd number : ', odd_count)

question02((1, 2, 3, 4, 5, 6, 7, 8, 9))


# 3. Write a Python program which iterates the integers from 0 to 50. For 
# multiples of three print "Fizz" instead of the number and for the multiples 
# of five print "Buzz". For numbers which are multiples of both three and five 
# print "FizzBuzz".

# Expected Output :

# fizzbuzz
# 1
# 2 
# fizz
# 4
# buzz
# ...

def question03():
    for i in range(50): # Here, I assume 50 is not included.
        if i % 3 == 0 and i % 5 == 0:
            print ('fizzbuzz')
        elif i % 3 == 0:
            print ('fizz')
        elif i % 5 == 0:
            print ('buzz')
        else:
            print (i)
            
question03()


# 4. Given a list iterate it and display numbers which are divisible by 5 and 
# if you find number greater than 150 stop the loop iteration
# list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

# Expected output:
# 15
# 55
# 75
# 150

def question04(input_list):
    for i in input_list:
        if i % 5 == 0 and i <= 150:
            print (i)
        else:
            continue

list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]        
question04(list1)


# 5. Pick one of the questions above and use range() for a different solution
# I choose Question 4

def question05(input_list):
    for i in range(len(input_list)):
        if input_list[i] % 5 == 0 and input_list[i] <= 150:
            print (input_list[i])
        else:
            continue

list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]        
question05(list1)



# 6. Pick one of the question above and use comprehensions for a different solution.
# I choose Question 1

def question06():    
    numList = [num for num in range(1500,2701) if num%5 == 0 and num%7 == 0]
    print (numList)

question06()


# --------------------------------------------------------------------------------------

# Exercise 06

# Question 01
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
    
def calculation(a, b):
    sum_ab = a + b
    substract_ab = a - b
    
    return sum_ab, substract_ab

res = calculation(40,10)
print(res)


# Question 02
	'''
	Return a lambda object that takes in a base and height of triangle
	and computes the area.

	Arguments:
	None

	Returns:
	lambda_triangle_area: the lambda
	'''
   	# code up your solution here

triangle_lambda = lambda h, b: print('lambda_triangle_area: ', 0.5*h*b)
triangle_lambda(1, 1)


# Question 03
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
    word = sorted(hyphen_str.split('-'))
    print ('-'.join(word))

sort_words('green-red-yellow-black-white')


# Question 04
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

def perfect_number(number):
    divisor_sum = 0
    for num in range(1, number):
        if number % num == 0:
            divisor_sum += num
    
    if divisor_sum == number:
        print ('The number, {} is perfect.'.format(number))

perfect_number(6)






















