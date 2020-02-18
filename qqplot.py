#!/usr/bin/env python
# coding: utf-8

# ### QQ plot for Normal vs Weibull distribution

# In[60]:


#get_ipython().magic(u'reset')


# In[61]:


import numpy as np 
import statsmodels.api as sm 
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':20})


# In[62]:


n=input('Enter number of random data points = ')
data_points = np.random.normal(0, 1, n)     
normal_data=sorted(data_points)  


# In[63]:
print('**************************************************')
print('Weibull distribution')
a=input('Enter value of shape parameter =  ')
#a = 2. # shape
weibull_points = np.random.weibull(a, n)


# In[64]:


sorted_weibull=sorted(weibull_points)


# In[ ]:





# In[65]:


plt.rc('font', family='serif')
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(1, 1, 1)

line, = ax.plot(sorted_weibull,normal_data,'*-')
plt.grid()
plt.xlabel('Weibull distribution data')
plt.ylabel('Normal distribution data')
plt.title('QQ plot, a='+str(a))
plt.show()


# In[ ]:




