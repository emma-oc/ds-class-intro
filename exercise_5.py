'''
Edit this file to complete Exercise 5
'''

# 1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5,
# between 1500 and 2700 (both included).

# code up your solution here
num_list = []
for num in range(1500,2701):
    if num % 7 == 0 and num % 5 == 0:
        num_list.append(num)
print(num_list)

# 2. Write a Python program to count the number of even and odd numbers from a series of numbers.

# example: numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# output:
# >>> Number of even numbers : 4
# >>> Number of odd numbers : 5

# code up your solution here
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

even_num = 0
odd_num = 0
for num in numbers:
    if num % 2 == 0:
        even_num += 1
    else:
        odd_num += 1

print("Number of even numbers :{0}\nNumber of odd numbers :{1}".format(even_num,odd_num))

# 3. Write a Python program which iterates the integers from 0 to 50.
# For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

# Expected Output :
# >>> fizzbuzz
# >>> 1
# >>> 2
# >>> fizz
# >>> 4
# >>> buzz
# >>> ...

# code up your solution here
for i in range(51):
    if i % 15 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)

# 4. Given a list iterate it and display numbers which are divisible by 5 and
# if you find number greater than 150 stop the loop iteration

# examples: list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
# output:
# >>> 15
# >>> 55
# >>> 75
# >>> 150

# code up your solution here
list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
for i in list1:
    if i % 5 == 0:
        if i > 150:
            break
        print(i)


# 5. Pick one of the questions above and use range() for a different solution

# code up your solution here
# Q2
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

even_num = 0
odd_num = 0
for num in range(1,10):
    if num % 2 == 0:
        even_num += 1
    else:
        odd_num += 1
print("Number of even numbers :{0}\nNumber of odd numbers :{1}".format(even_num,odd_num))


# 6. Pick one of the question above and use comprehension for a different solution

# code up your solution here
# Q1
new_list = [num for num in range(1500,2701)if num % 7 == 0 and num % 5 == 0]
print(new_list)

# 7. Pick one of the questions above and use while loop for a different solution

# code up your solution here
# Q4
list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
count = 0
while list1:
    if list1[count] % 5 == 0:
        if list1[count] > 150:
            break
        print(list1[count])
    count += 1

