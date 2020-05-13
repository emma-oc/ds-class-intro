#!/usr/bin/env python
# coding: utf-8

# Exercise 5. Find the mean and standard deviation of math and verbal SAT score for men-only, women-only, and non gender specific universities.¶

# In[2]:


import pandas as pd


# In[6]:


df = pd.read_csv("college.csv")


# In[11]:


df.groupby(['menonly','womenonly']).agg({'satvrmid': ['mean', 'std'],
                                               'satmtmid': ['mean', 'std']})


# Exercise 6. Find the top 3 universities with largest numbers of undergraduate students for each state¶

# In[26]:


df['rank'] = df.sort_values(['ugds'], ascending=False).groupby('stabbr').cumcount()+1


# In[28]:


df.sort_values(['stabbr','rank']).query('rank<4')


# Exercise 7. Generate a DataFrame for the ratios of (number of employees of specific gender and race/total number of employees) for all race-gender combinations

# In[30]:


df2 = pd.read_csv('employee.csv')


# In[64]:


df3= df2.groupby(['race','gender']).title.count()


# In[65]:


total = df2.agg({'title':'count'})


# In[66]:


df4 = df3.map(lambda x: x/total)


# In[67]:


df4


# Exercise 8. Use pd.melt() to unpivot table pv3 to the format of pv4 in exampel above

# In[69]:


pv3 = df2.pivot_table(index='gender', columns='race', 
                      values='salary', aggfunc='mean').round(-3).reset_index()


# In[70]:


pv3


# In[83]:


pv4 = pd.melt(pv3, id_vars = [('gender')])


# In[84]:


pv4


# In[ ]:




