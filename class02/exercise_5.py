'''
Edit this file to complete Exercise 5
'''

# 1. write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).

# code up your solution here
num = []
for i in range(1500,2700):
    if i%7 == 0 and i%5 == 0:
        num.append(i)
print(num)
        

# 2. Write a Python program to count the number of even and odd numbers from a series of numbers.

# example: numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# output:
# >>> Number of even numbers : 4
# >>> Number of odd numbers : 5

# code up your solution here
even=0
odd=0
numbers = (1,2,3,4,5,6,7,8,9,10)
for i in numbers:
    if i%2 == 0:
        even+=1
    else:
        odd+=1
print("Number of even numbers:",even)
print("Number of odd numbers:", odd)
        


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

for i in range(0,50):
    if i%3 == 0 and i%5 ==0:
        print('FizzBuzz')
    elif i%5 == 0:
        print('Buzz')
    elif i%3 == 0:
        print('Fuzz')
    
        



# 4. Given a list iterate it and display numbers which are divisible by 5 and if you find number greater than 150 stop the loop iteration

# examples: list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
# output:
# >>> 15
# >>> 55
# >>> 75
# >>> 150

# code up your solution here

list = [15,20,23,25,57,46,47,40,50,80,90,120,123,125,135,150,223534667]
for i in list:
    if i <150:
        if i%5==0:
            print (i)


# 5. Pick one of the questions above and use range() for a different solution

# code up your solution here


for i in range(1,152):
    if i<150:
        if i%5 ==0:
            print(i)

# 6. Pick one of the question above and use comprehension for a different solution

# code up your solution here

