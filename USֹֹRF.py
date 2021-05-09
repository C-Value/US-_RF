#!/usr/bin/env python
# coding: utf-8

# In[10]:


import quandl 
quandl.ApiConfig.api_key = 'W1Y9RrxN2LYQ9kpyxVGF'
quandl.get('USTREASURY/YIELD', start_date='2018-12-31', end_date='2020-12-31')

