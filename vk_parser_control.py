#!/usr/bin/env python
# coding: utf-8

# In[8]:


import vk
import numpy as np
import pandas as pd


# In[9]:


get_ipython().run_line_magic('run', 'vk_parser.py')


# In[10]:


def control(token,group,number,format_file):
    token_init(token)
    ids=get_members(group) #short name or id of required group
    arrays_init(number) #give file with ids
    index(ids) #give file with ids
    sorting(number) #give number of people to sort
    data_init() #give file with ids
    export(format_file)


# In[14]:


if __name__ == "__main__":
    token = "" #enter your token
    control(token,"", , "")#enter groupid, number of people to sort, file format to save data 


# In[15]:


pd.read_csv('database.csv')


# In[ ]:




