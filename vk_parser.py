#!/usr/bin/env python
# coding: utf-8

# In[23]:


import vk
import numpy as np
import pandas as pd
data = pd.DataFrame(columns=['ids', 'first_name', 'last_name', 'is_closed', 'bdate', 'sex', 'city_id', 'country_id' ])


# In[24]:


def token_init(token): 
    global vk_api
    session = vk.Session(access_token=token)
    vk_api = vk.API(session)


# In[25]:


def get_members(groupid): #create list of ids of reqired group
    first = vk_api.groups.getMembers(group_id=groupid, v=5.92)
    group_m = first["items"]  
    count = np.floor_divide(first["count"],1000)
    
    for i in range(1, count+1):  
        group_m = group_m + vk_api.groups.getMembers(group_id=groupid, v=5.92, offset=i*1000)["items"]
    return group_m


# In[26]:


def arrays_init(number):
    global ids_new
    ids_new = pd.Series(number)
    global first_names
    first_names = pd.Series(number, dtype=object)
    global last_names
    last_names=pd.Series(number, dtype=object)
    global bdates
    bdates = pd.Series(number, dtype=object)
    global sex 
    sex = pd.Series(number, dtype=np.int64)
    global city_ids
    city_ids = pd.Series(number, dtype=np.int64)
    global country_ids
    country_ids = pd.Series(number, dtype=np.int64)
    global is_closeds
    is_closeds = pd.Series(number,dtype=bool)#create list of indexes for providing users.get


# In[27]:


def index(ids_file):
    global data1
    data1 = []
    count= np.floor_divide(len(ids_file), 900)
    index=np.zeros((count+1,2))
    
    for i in range(count):
        index[(i,0)]=i*900
        index[(i,1)]=(i+1)*900
    index[(count,0)]=count*900
    index[(count,1)]=len(ids_file)
    
    for i in range(count+1):
        data1[int(index[(i,0)]):int(index[(i,1)])] = vk_api.users.get(user_ids=ids_file[int(index[(i,0)]):int(index[(i,1)])],fields = 'bdate, city, country, sex', v=5.92)


# In[28]:


def sorting(number):
    for i in range(number):
        try:
            ids_new[i] = data1[i]['id']
            first_names[i] = data1[i]['first_name']
            last_names[i] = data1[i]['last_name']
            sex[i] = data1[i]['sex']
            is_closeds[i] = data1[i]['is_closed']
            city_ids[i] = data1[i]['city']['id']
            country_ids[i] = data1[i]['country']['id']
            bdates[i]= data1[i]['bdate']
        except KeyError:
            pass


# In[31]:


def data_init():    
    data['ids']=ids_new
    data['first_name'] = first_names
    data['last_name'] = last_names
    data['sex'] = sex
    data['city_id'] = city_ids
    data['country_id'] = country_ids
    data['is_closed'] = is_closeds
    data['bdate'] = bdates


# In[29]:


def export(format_file):
    if format_file == "csv":
        data.to_csv("database.csv", index=False)
    elif format_file == "excel":
        data.to_excel("database.xlsx", index=False)
    else:
        print("Wrong format")

