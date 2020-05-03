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

    add = a+b
    diff = a-b
    return add,diff
    
res = calculation(40, 10)
print(res)


def triangle_lambda():
    '''
    Return a lambda object that takes in a base and height of triangle
    and computes the area.
        
    Arguments:
    None
    
    Returns:
    lambda_triangle_area: the lambda
    '''
    
    # code up your solution here 
    
    area = lambda x,y : x*y*0.5
    
print(area(10,5))


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
    
    x = hyphen_str.split("-")
    x.sort()
    y = print("-".join(x))
    return y

sort_words('green-red-yellow-black-white')       


def perfect_number(a):
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
    
    divisor = []
    for i in range(1,a+1):
        if a%i == 0:
            divisor.append(i)
    if sum(divisor)/2 == a:
        return True
    else:
        return False

print(perfect_number(8128))

    
    
if __name__ == '__main__':
	pass