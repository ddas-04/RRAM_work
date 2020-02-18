#!/usr/bin/env python
# coding: utf-8

# ### QQ plot for Normal vs Weibull distribution

# In[60]:


#get_ipython().magic(u'reset')


# In[61]:


import numpy as np 
import statsmodels.api as sm 
import matplotlib.pyplot as plt
import random
plt.rcParams.update({'font.size':20})


# In[62]:


n=input('Enter number of random data points = ')
n=int(n)
np.random.seed(1)
data_points = np.random.normal(0, 1, n)
normal_data=sorted(data_points)  


# In[63]:
print('**************************************************')
print('Weibull distribution')
# a=input('Enter value of shape parameter =  ')

a=np.linspace(2,10,17)
#a=int(a)

for i in range(len(a)):
    np.random.seed(1)
    weibull_points = np.random.weibull(a[i], n)
    sorted_weibull = sorted(weibull_points)
    plt.rc('font', family='serif')
    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(1, 1, 1)
    line, = ax.plot(sorted_weibull,normal_data,'*-')
    plt.grid()
    plt.xlabel('Weibull distribution data')
    plt.ylabel('Normal distribution data')
    plt.title('QQ plot, a='+str(a[i]))
    plt.savefig('fig'+str(i)+'.png')


plt.show()


# In[ ]:




