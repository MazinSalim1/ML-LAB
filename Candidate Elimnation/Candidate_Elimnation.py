#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[17]:


data = pd.read_csv('canelim.csv')

concept = np.array(data)[:,:-1]
target = np.array(data)[:,-1]


# In[24]:


data
#concept
#target


# In[53]:


def train(con,tar):
    specific_h = con[0].copy()
    general_h=[['?' for x in range(len(specific_h))] for x in range(len(specific_h))]
    #print(general_h)
    
    #checking for the +ve instance ie the target is yes 
    for i,val in enumerate(con):
        if tar[i] == 'yes':
            for x in range(len(specific_h)):
                if(val[x] != specific_h[x]):
                    specific_h[x] = '?'
                    general_h[x][x] = '?'
                    #print(specific_h[x])
                    #print(general_h[x][x])
        else:
        #checking for the -ve instance ie the target no    
             for x in range(len(specific_h)):
                if val[x] != specific_h[x]:
                    general_h[x][x] = specific_h[x]
                    print(general_h[x][x])
                else:
                    general_h[x][x]='?'
                    #print(general_h[x][x])
                    
        #Outlining the outputs in terms of iteration            
        print("Iteration["+ str(i+1) + "]")
        print("Specific: "+str(specific_h))
        print("General: "+str(general_h)+"\n\n")
   

    
    general_h =[general_h[i] for i, val in enumerate(general_h) if val!= ['?' for x in range(len(specific_h))]]
        
    return specific_h, general_h


# In[54]:


specific , general = train(concept,target)
print("Final hypothesis: ")
print("Specific hypothesis: " +str(specific))
print("General hypothses: "+ str(general))


# In[55]:


train(concept,target)


# In[ ]:




