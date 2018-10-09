
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import requests
import pickle
import operator
import time


# In[2]:


def load_dict():
    file = open('stock_dict.pickle', 'rb')
    data = pickle.load(file)
    file.close()
    return data

def load_set():
    file = open('stock_set.pickle','rb')
    data = pickle.load(file)
    file.close()
    return data


# In[3]:


ticker_set = load_set()
stock_data = load_dict()


# In[17]:


ticker = "ALT"
df_temp = pd.read_json('https://api.iextrading.com/1.0/stock/'+ticker+'/chart/1M')


print(df_temp)
  
# ALT
# TZA
# NBEV
# PCG
# USDCAD
# AAXN
# SPX
# TWTR

