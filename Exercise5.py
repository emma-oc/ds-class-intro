#!/usr/bin/env python
# coding: utf-8

# 5.1

# In[19]:


result = []

for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        result.append(i)

print(result)


# 5.2

# In[11]:


numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
odd_count = 0
even_count = 0
for i in numbers:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print('number of even numbers: {}'.format(even_count))
print('number of odd numbers: {}'.format(odd_count))


# 5.3

# In[13]:


for i in range(0, 51):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
        


# 5.4

# In[16]:


list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

for i in list1:
    if i > 150:
        break
    elif i % 5 == 0:
        print(i)
    else:
        continue
            


# 5.5
# pick 5.2

# In[18]:


odd_count = 0
even_count = 0
for i in range(1, 10):
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
        
print('number of even numbers: {}'.format(even_count))
print('number of odd numbers: {}'.format(odd_count))


# 5.6 pick 5.1

# In[28]:


print([number for number in range(1500, 2701) if number % 7 == 0 and number % 5 ==0])


# 5.7 pick 5.3

# In[29]:


count = 0
while count < 51:
    if count % 3 == 0 and count % 5 == 0:
        print('FizzBuzz')
    elif count % 3 == 0:
        print('Fizz')
    elif count % 5 == 0:
        print('Buzz')
    else:
        print(count)
    
    count += 1


# In[ ]:




