'''
Edit this file to complete Exercise 5
'''

# 1. write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).

# code up your solution here
list = []
for num in range(1500, 2701):
    if num % 5 == 0 and num % 7 == 0:
        list.append(num)
print(list)


# 2. Write a Python program to count the number of even and odd numbers from a series of numbers.

# example: numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# output:
# >>> Number of even numbers : 4
# >>> Number of odd numbers : 5

# code up your solution here
numbers = range(1, 20)
odd = []
even = []
for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print('Number of even numbers : {}'.format(even))
print('Number of even numbers : {}'.format(odd))



# 3. Write a Python program which iterates the integers from 0 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

# Expected Output :
# >>> fizzbuzz
# >>> 1
# >>> 2
# >>> fizz
# >>> 4
# >>> buzz
# >>> ...

# code up your solution here

for num in range(0, 51):
    if num % 3 == 0 and num % 5 != 0:
        print('Fizz')
    elif num % 5 == 0 and num % 3 != 0:
        print('Buzz')
    elif num % 5 == 0 and num % 3 == 0:
        print('FizzBuzz')
    else:
        print(num)



# 4. Given a list iterate it and display numbers which are divisible by 5 and if you find number greater than 150 stop the loop iteration

# examples: list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
# output:
# >>> 15
# >>> 55
# >>> 75
# >>> 150

# code up your solution here

list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

for num in list1:
    if num > 150:
        break
    if num % 5 == 0:
        print(num)


# 5. Pick one of the questions above and use range() for a different solution

# code up your solution here

#I already used the range().


# 6. Pick one of the question above and use comprehension for a different solution

# code up your solution here

anslist = [num for num in range(1500, 2701) if num % 5 == 0 and num % 7 == 0 ]
print(anslist)


# 7. Pick one of the questions above and use while loop for a different solution

# code up your solution here
num = 0
while num <= 50:
    if num % 3 == 0 and num % 5 != 0:
        print('Fizz')
    elif num % 5 == 0 and num % 3 != 0:
        print('Buzz')
    elif num % 5 == 0 and num % 3 == 0:
        print('FizzBuzz')
    else:
        print(num)
    num += 1
