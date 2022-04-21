#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pandas as pd
import numpy as np

#reading the csv file
data = pd.read_csv('data.csv')
data


# In[25]:


#Slicing all the concept other than last
concepts = np.array(data)[:,:-1]
concepts


# In[26]:


#Output column and enumerate it 
target = np.array(data)[:,-1]
target
specific_h=[]


# In[35]:


def train(con, tar):
    for i, val in enumerate(tar):
        if val.lower() == 'yes':
            specific_h = con[i].copy()
            print(specific_h)
            
            break
                
    for i, val in enumerate(con):
        if tar[i].lower() == 'yes':
            for x in range(len(specific_h)):
                if val[x] != specific_h[x]:
                    specific_h[x] = '?'
                else:
                    pass
    return specific_h
     


# In[36]:


print(train(concepts,target))

