import os.path
import csv
import json

'''
Edit this file to complete Exercise 5
'''

# 1. Write a Python program to find those numbers which
# are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).

# code up your solution here


def question1():
    for i in range(1500, 2701):
        if i % 7 == 0 and i % 5 == 0:
            print(i)


question1()


# 2. Write a Python program to count the number of
# even and odd numbers from a series of numbers.
# example: numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# output:
# >>> Number of even numbers : 4
# >>> Number of odd numbers : 5
# code up your solution here


def question2():
    numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    print('Number of even numbers:', len([i for i in numbers if i % 2 == 0]))
    print('Number of odd numbers:', len([i for i in numbers if i % 2 != 0]))


question2()


# 3. Write a Python program which iterates the integers
# from 0 to 50. For multiples of three print "Fizz"
# instead of the number and for the multiples of five
# print "Buzz". For numbers which are multiples of both
# three and five print "FizzBuzz".

# Expected Output :
# >>> fizzbuzz
# >>> 1
# >>> 2
# >>> fizz
# >>> 4
# >>> buzz
# >>> ...

# code up your solution here
def question3():
    for i in range(0, 51):
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        else:
            print(i)


question3()


# 4. Given a list iterate it and display numbers
# which are divisible by 5 and if you find number
# greater than 150 stop the loop iteration

# examples: list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
# output:
# >>> 15
# >>> 55
# >>> 75
# >>> 150

# code up your solution here
def question4():
    list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
    for i in list1:
        if i % 5 == 0 and i <= 150:
            print(i)


question4()


# 5. Pick one of the questions above and use range() for a different solution

# code up your solution here
def question5():
    print([i for i in range(0, 200) if i % 5 == 0 and i <= 150])


question5()


# 6. Pick one of the question above and use comprehension
# for a different solution

# code up your solution here
def question6():
    list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
    print([i for i in list1 if i % 5 == 0 and i <= 150])


question6()


# 7. Pick one of the questions above and use while loop for
# a different solution

def question7():
    list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
    i = 0
    while i < len(list1):
        if list1[i] <= 150 and list1[i] % 5 == 0:
            print(list1[i])
        i += 1


question7()


'''
Edit this file to complete Exercise 6
'''

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
    return(a + b, abs(a - b))


res = calculation(40, 10)
print(res)


'''
Return a lambda object that takes in a base and height of triangle
and computes the area.
Arguments:
None
Returns:
lambda_triangle_area: the lambda
'''


def triangle_lambda():
    return lambda x, y: (x * y / 2)


triangle_lambda()(2, 3)


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
    items = [n for n in hyphen_str.split('-')]
    items.sort()
    return ('-'.join(items))


sort_words('green-red-yellow-black-white')


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


def perfect_number(x):
    divisor = []
    for i in range(1, x + 1):
        if int(x) % i == 0:
            divisor.append(i)
    if sum(divisor) / 2 == x:
        return True
    else:
        return False


if __name__ == '__main__':
    pass


perfect_number(6)
perfect_number(497)


'''
Edit this file to complete Exercise 7
'''

# import the modules you need here


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


def check_path(path):
    abs_ = True
    dir_ = True
    file = True
    if os.path.exists(path):
        if not os.path.isabs(path):
            abs_ = False
        if not os.path.isdir(path):
            dir_ = False
        if not os.path.isfile(path):
            file = False
        return(True, [abs_, dir_, file])
    else:
        return(False, [])


check_path('/Users/helenmonster/Desktop/UNI/')


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
# os.getcwd()
# '/Users/helenmonster/Desktop/UNI/Career/DataScience/ds-class-intro/class03'
# os.chdir('/Users/helenmonster/Desktop/UNI/Career/DataScience/
# ds-class-intro/class03')


def read_csv(file):
    count = 0
    with open(file, 'r') as f:
        for line in f:
            count += 1
    return count


read_csv('AMZN.csv')


'''
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
'''

# code up your solution here


def write_csv(data_list, output_file):
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        for row in data_list:
            writer.writerow(row)


data_list = [(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12)]
write_csv(data_list, 'example.csv')


'''
reads a JSON file and return its contents as a dictionary

Arguments:
file: path to the file to read

Returns:
A dictionary containing JSON contents

Example:
read_json('some.json')
>>> [{'name': 'emma', 'skill': {'coding1': 'python',
#  'coding2': 'r'}, 'role': 0}]
'''

# code up you solution here


def read_json(file):
    with open(file) as f:
        js = json.load(f)
    print(js)


read_json('some.json')


if __name__ == "__main__":
    pass
