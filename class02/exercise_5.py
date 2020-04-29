'''
Edit this file to complete Exercise 5
'''

# 1. rite a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).

    Solution 1:
    
    answerlist=list()
    for a in range(1500,2701):
        if a%5==0 and a%7==0:
            answerlist.append(a)
        else:
            pass
    print(answerlist)
    
    Solution 2:
    
    answerlist=list()
    for a in range(1505,2701,35)
        answerlist.append(a)
    print(answerlist)            





# 2. Write a Python program to count the number of even and odd numbers from a series of numbers.

# example: numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# output:
# >>> Number of even numbers : 4
# >>> Number of odd numbers : 5

evenlist=list()
oddlist=list()

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
for a in numbers:
    if a%2==0:
        evenlist.append(a)
    else:
        oddlist.append(a)

print("number of even nubmers : "+ str(len(evenlist)))
print("number of odd nubmers : "+ str(len(oddlist)))





# 3. Write a Python program which iterates the integers from 0 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

# Expected Output :
# >>> fizzbuzz
# >>> 1
# >>> 2
# >>> fizz
# >>> 4
# >>> buzz
# >>> ...

for a in range(0,51):
    if a%15==0:
        print("fizzbuzz")
    elif a%5==0:
        print("buzz")
    elif a%3==0:
        print("fizz")
    else:
        print(a)




# 4. Given a list iterate it and display numbers which are divisible by 5 and if you find number greater than 150 stop the loop iteration

# examples: list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
# output:
# >>> 15
# >>> 55
# >>> 75
# >>> 150

for a in list1:
    if a<=150:
        if a%5==0:
            print(a)
        else:
            pass
    else:
        pass
 
        




# 5. Pick one of the questions above and use range() for a different solution

print([a for a in range(1505,2701,35)])


# 6. Pick one of the question above and use comprehension for a different solution

print([a for a in range(1505,2701,35)])



# 7. Pcik one of the questions above and use while loop for a different solution

answerlist=[]
i = 1500 # iter/i iteration
while i < 2701:
    if i%5==0 and i%7==0:
        answerlist.append(i)
    i += 1
        
print(answerlist)

