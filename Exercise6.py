#!/usr/bin/env python
# coding: utf-8

# Exercise 6

# In[1]:


def calculation(a, b):
    addition = a + b
    subtraction = a - b
    return addition, subtraction


# In[2]:


res = calculation(40, 10)
print(res)


# In[5]:


def sort_words(hyphen_str):
    txt = hyphen_str.split('-')
    txt.sort()
    print('-'.join(txt))

sort_words('green-red-yellow-black-white')


# In[15]:


test_number = 8128

def perfect_number():
    perfect = False
    i = 1
    divisors = []
    while i < test_number:
        if test_number % i == 0:
            divisors.append(i)
        i += 1
    
    if test_number == sum(divisors):
        perfect = True
    
    return perfect
 
perfect_number()


# In[1]:


triangle_lambda = lambda x,y: 1/2 * x * y


# In[2]:


triangle_lambda(3, 4)


# In[ ]:




