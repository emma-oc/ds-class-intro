'''
Edit this file to complete Exercise 5
'''

# 1. rite a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).

# code up your solution here
c=[]
for i in range(1500,2701):
    if i%5==0 and i%7==0:
        c.append(i)
print(c)    




# 2. Write a Python program to count the number of even and odd numbers from a series of numbers.

# example: numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# output:
# >>> Number of even numbers : 4
# >>> Number of odd numbers : 5

# code up your solution here

numbers=(1,2,3,4,5,6,7,8,9)
even=0
odd=0
for i in numbers:
    if i%2==0:
        even+=1
    elif i%2==1:
        odd+=1
print("Number of even numbers:{even}".format(even=even))
print("Number of even numbers:{odd}".format(odd=odd))


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

i=0
while i <=50:
    if i%15==0:
        print('FizzBuzz')
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else:
        print(i)
    i+=1



# 4. Given a list iterate it and display numbers which are divisible by 5 and if you find number greater than 150 stop the loop iteration

# examples: list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
# output:
# >>> 15
# >>> 55
# >>> 75
# >>> 150

# code up your solution here

list1 = [12, 15,32, 42, 55, 75, 122, 132, 150, 180, 200]
for i in list1:
    if i>150:
        break
    elif i%5==0:
        print(i)
    else:
        continue


# 5. Pick one of the questions above and use range() for a different solution

# code up your solution here
for i in range(0,51):
    if i%15==0:
        print('FizzBuzz')
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else:
        print(i)
    i+=1
        



# 6. Pick one of the question above and use comprehension for a different solution

# code up your solution here

print(['fizzbuzz' if i%15==0 else 'fizz' if i%3==0 else 'buzz' if i&5==0 else i for i in range(0,51)])


# 7. Pcik one of the questions above and use while loop for a different solution

# code up your solution here

i=0
while i <=50:
    if i%15==0:
        print('FizzBuzz')
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else:
        print(i)
    i+=1
