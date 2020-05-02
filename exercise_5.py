#!/usr/bin/env python
# coding: utf-8

# In[10]:


# 1.  Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).

# code up your solution here

list1 = []
for i in range(1500, 2701):
    if i % 7 == 0 and i %5 ==0:
        list1.append(i)
print(len(list1))
list1[:5]


# In[6]:


# 2. Write a Python program to count the number of even and odd numbers from a series of numbers.

# example: numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# output:
# >>> Number of even numbers : 4
# >>> Number of odd numbers : 5

# code up your solution here

counter_even=0
counter_odd=0
list2=[1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in list2:
    if i%2==0:
        counter_even+=1
    else:
        counter_odd+=1
print(counter_even)
print(counter_odd)


# In[11]:


# 3. Write a Python program which iterates the integers from 0 to 50. 
# For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

# Expected Output :
# >>> fizzbuzz
# >>> 1
# >>> 2
# >>> fizz
# >>> 4
# >>> buzz
# >>> ...

# code up your solution here
for i in range(0, 51):
    if i % 15==0:
        print('FizzBuzz')
    elif i % 3==0:
        print('Fizz')
    elif i % 5==0:
        print('Buzz')
    else:
        print(i)


# In[13]:


# 4. Given a list iterate it and display numbers which are divisible by 5 and if you find number greater than 150 stop the loop iteration

# examples: list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

list3 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]


for i in list3:
    if i%5==0:
        if i <= 150:
            print(i)
        else:
            break


# In[16]:


# 5. Pick one of the questions above and use range() for a different solution

# code up your solution here


# 4:
list4 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]


for i in range(len(list3)):
    if list3[i]%5==0:
        if list3[i] <= 150:
            print(list3[i])
        else:
            break


# In[34]:


# 6. Pick one of the question above and use comprehension for a different solution

# code up your solution here

# 1:
list5 = [i for i in range(1500, 2701) if i % 7 == 0 and i %5 ==0]

list5[:5]


# In[35]:


# 7. Pcik one of the questions above and use while loop for a different solution

# code up your solution here

#3:
i=0
while i <=50:
    if i % 15==0:
        print('FizzBuzz')
    elif i % 3==0:
        print('Fizz')
    elif i % 5==0:
        print('Buzz')
    else:
        print(i)
    i+=1

