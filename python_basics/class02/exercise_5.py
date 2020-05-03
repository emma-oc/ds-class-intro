'''
Edit this file to complete Exercise 5
'''
## Michael (Jinghan Chen)
# 1. write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).

start = 1500
end = 2700
nums = []
for x in range(start, end + 1):
    if (x % 7 == 0) and (x % 5 == 0):
        nums.append(x)
print(nums)

# 2. Write a Python program to count the number of even and odd numbers from a series of numbers.

# example: numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# output:
# >>> Number of even numbers : 4
# >>> Number of odd numbers : 5

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
count_even = 0
count_odd = 0
for x in numbers:
    if x % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
print("Number of even numbers : " + str(count_even))
print("Number of odd numbers : " + str(count_odd))

# 3. Write a Python program which iterates the integers from 0 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

# Expected Output :
# >>> fizzbuzz
# >>> 1
# >>> 2
# >>> fizz
# >>> 4
# >>> buzz
# >>> ...

for i in range(51):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# 4. Given a list iterate it and display numbers which are divisible by 5 and if you find number greater than 150 stop the loop iteration

# examples: list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
# output:
# >>> 15
# >>> 55
# >>> 75
# >>> 150

list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
for i in list1:
    if i > 150:
        break
    elif i % 5 == 0:
        print(i)
        
# 5. Pick one of the questions above and use range() for a different solution
# used range in question 1 and 3 

# 6. Pick one of the question above and use comprehension for a different solution

newList = [i for i in range(start, end + 1) if (x % 7 == 0) and (x % 5 == 0)]
print(newList)

# 7. Pick one of the questions above and use while loop for a different solution
# 3
i = 0
while i <= 50:
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    i += 1
