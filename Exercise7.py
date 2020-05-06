#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os


# In[13]:



os.chdir('C:\\Users\\shifs\\Documents\\Github')
os.getcwd()


# In[8]:


import os
path = '/home/User/Documents'
ispath = os.path.exists(path)
ispath


# In[10]:


import os
path = 'some/path/of/a/directory'

def check_path(path):
    bool_list = []
    result = False
    if os.path.exists(path) == False:
        pass
    else:
        result = True
        bool_list = [False, False, False]
        if os.path.isfile(path) == True:
            bool_list[2] = True
        else:
            if os.path.isabs(path) == True:
                bool_list[0] = True
            else:
                bool_list[1] = True
    
    return result, bool_list
            
check_path(path)


# In[16]:


import csv
file = 'AMZN.csv'
def read_csv(file):
    with open(file, 'r') as f:
        reader = reader = csv.reader(f, delimiter=',')
        count = 0
        for row in reader:
            count += 1
    
    return count

num_line = read_csv(file)
num_line


# In[24]:


import csv

data_list = [(1,2,3,4), (5,6,7,8), (9,10,11,12)]
def write_csv(data_list, output_file):
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        for row in data_list:
            writer.writerow(row) 
        
write_csv(data_list, 'example_file')


# In[28]:


import json

def read_json(file):
    with open(file) as f:
        js = json.load(f)
    
    return js
    
result = read_json('some.json') 
print(result)


# In[ ]:




