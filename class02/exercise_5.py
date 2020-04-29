'''
Edit this file to complete Exercise 5
'''

# 1. rite a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).

# code up your solution here
print('Question 1')
list1 = []
for num in range(1500, 2701):
    if num % 5 == 0 and num % 7 == 0:
        list1.append(num)
print(list1)
print('\n')




# 2. Write a Python program to count the number of even and odd numbers from a series of numbers.

# example: numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# output:
# >>> Number of even numbers : 4
# >>> Number of odd numbers : 5

# code up your solution here
print('Question 2')
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_num = odd_num = 0
for num in list2:
    if num % 2 == 0:
        even_num += 1
    else:
        odd_num += 1
print('Number of even numbers:', even_num, '\nNumber of odd numbers:', odd_num)
print('\n')



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
print('Question 3')
for i in range(51):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
print('\n')





# 4. Given a list iterate it and display numbers which are divisible by 5 and if you find number greater than 150 stop the loop iteration

# examples: list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
# output:
# >>> 15
# >>> 55
# >>> 75
# >>> 150

# code up your solution here
print('Question 4')
list3 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
for num in list3:
    if num > 150:
        break
    if num % 5 == 0:
        print(num)
print('\n')



# 5. Pick one of the questions above and use range() for a different solution

# code up your solution here
print('Question 5')
even_num = odd_num = 0
for num in range(1, 10):
    if num % 2 == 0:
        even_num += 1
    else:
        odd_num += 1
print('Number of even numbers:', even_num, '\nNumber of odd numbers:', odd_num)
print('\n')



# 6. Pick one of the question above and use comprehension for a different solution

# code up your solution here
print('Question 6')
print([num for num in list3 if num % 5 == 0 and num <= 150])
print('\n')


# 7. Pcik one of the questions above and use while loop for a different solution

# code up your solution here
print('Question 7')
i = 0
while i <= 50:
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
    i += 1
