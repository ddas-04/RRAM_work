#!/usr/bin/env python
# coding: utf-8

# ## RRAM Stanford model data extraction

# In[103]:


#get_ipython().magic(u'reset')


# In[104]:


import numpy as np
import matplotlib.pyplot as plt
import xlrd 
from scipy import stats
import scipy.stats as st
import probscale
plt.rcParams.update({'font.size':20})


# In[105]:


#.xlsx file which contains the extracted data from the paper
loc=('./Default Dataset.xlsx') 


# In[106]:


wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0)


# In[107]:


n=sheet.nrows


# ### Resistance Values

# In[108]:


R=np.zeros(n)
for i_rows in range(n):
    R[i_rows]=float(sheet.cell_value(i_rows,0))


# In[109]:


R


# ### $Z_{score}$ values

# In[110]:


Zscore=np.zeros(n)
for i_rows in range(n):
    Zscore[i_rows]=float(sheet.cell_value(i_rows,1))


# In[111]:


Zscore


# ### CDF is calculated from $Z_{Score}$

# In[112]:


CDF=st.norm.cdf(Zscore)


# In[113]:


CDF


# ### Plot of CDF vs R with y axis as linear

# In[129]:


plt.rc('font', family='serif')
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(1, 1, 1)

line, = ax.plot(R/1000,CDF*100,'v ')

ax.set_xscale('log')
plt.xlim([1,1e4])
plt.ylim([0,100])
plt.yticks([0,25,50,75,100])
plt.xlabel('R(in KOhm)')
plt.ylabel('CDF(%)')
plt.title('Extracted data-linear y scale')
plt.grid()
plt.show()


# ### Plot of CDF vs R in probplot

# In[130]:


fig = plt.figure(figsize=(10,8))
ax3=fig.add_subplot(1, 1, 1)

common_opts = dict(
    probax='y',
    datascale='log',
    datalabel='R(in KOhm)',
    scatter_kws=dict(marker='v', linestyle='none')
)
fig = probscale.probplot(R/1000, ax=ax3, plottype='prob',
                         problabel='Cumulative Probabilities(%)',  **common_opts)
ax3.set_xlim(left=2, right=1e4)
ax3.set_ylim(bottom=0.13, top=99.87)
ax3.grid()
plt.yticks([0.5,2,10,30,50,70,90,98,99.5])

plt.tight_layout()
plt.title('Extracted data-Probability y scale')
plt.show()


# ### Fitting Polynomial Equation

# In[116]:


poly_order=7 # Fitting Polynomial order
z = np.polyfit(R/1000, CDF, poly_order)


# In[117]:


R/1000


# In[118]:


z


# In[119]:


p = np.poly1d(z)


# In[120]:


print(np.poly1d(p))


# In[121]:


Rfit=np.linspace(12,105,101)


# In[122]:


CDFfit=p(Rfit)


# In[123]:


CDFfit


# In[136]:


fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(1, 1, 1)

line, = ax.plot(R/1000,CDF*100,'v ',label='data')
line, = ax.plot(Rfit,CDFfit*100,label='fit')

ax.set_xscale('log')
plt.xlim([1,1e4])
plt.ylim([0,100])
plt.xlabel('R(in KOhm)')
plt.ylabel('CDF(%)')
plt.grid()
plt.title('Original and Fitted plot')
ax.legend()
plt.show()


# ### PDF calculation by differentiating the CDF polynomial fit function

# ### Original Polynomial = $\sum\limits_{i=0}^n z[n-i]x^i$
# ### Differentiation = $\sum\limits_{i=1}^n iz[n-i] x^{i-1}$

# In[125]:


def PDF_fit(z,x,n):
    Val=0
    i=n
    while i>=1:
        Val=Val+i*z[n-i]*(x**(i-1))
        i=i-1
    
    return Val


# In[126]:


PDF_fit_value=np.zeros(len(Rfit))
for i in range(len(Rfit)):
    PDF_fit_value[i]=PDF_fit(z,Rfit[i],poly_order)

PDF_fit_value


# In[131]:


fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(1, 1, 1)

line, = ax.plot(Rfit,PDF_fit_value,'*-')
plt.xlabel('R(in KOhm)')
plt.ylabel('PDF')
plt.grid()
plt.title('Probability plot')
plt.show()


# In[ ]:




