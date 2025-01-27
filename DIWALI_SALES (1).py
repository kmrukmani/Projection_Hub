#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as plt


# In[21]:


df = pd.read_csv(r"D:\Rkumani\one drive\OneDrive\Desktop\DATA ANALYST\Diwali\Python_Diwali_Sales_Analysis-main\Python_Diwali_Sales_Analysis-main\Diwali Sales Data.csv",encoding = 'unicode escape')


# In[22]:


df.head()


# In[23]:


df.tail()


# In[24]:


df.head(10)


# In[26]:


df.tail(10)


# In[27]:


df.info()


# In[29]:


df.shape


# In[31]:


df.columns


# In[33]:


df.dtypes


# In[34]:


df.describe()


# In[35]:


df.isnull().sum()


# In[38]:


df.drop(['Status','unnamed1'], axis = 1,inplace = True)


# In[39]:


df.isnull().sum()


# In[40]:


df.dropna(inplace = True)


# In[41]:


df.info()


# In[42]:


df.isnull().sum()


# In[45]:


df.describe()


# In[48]:


df.describe(include = 'object')


# In[49]:


df.describe(include = 'float')


# In[52]:


df.describe(include = 'int')


# In[66]:


s = pd.DataFrame({'ananya':[11,12,13],'anisha tiwari':[11,12,13]})
s


# In[69]:


df['Amount']=df['Amount'].astype('int')


# In[70]:


df.info()


# In[72]:


df['Orders']=df['Orders'].astype('float')


# In[73]:


df.columns


# In[75]:


df.dtypes


# In[76]:


df['Orders']=df['Orders'].astype(int)


# In[77]:


df.info()


# In[78]:


df['Amount'].dtypes


# In[79]:


df['Orders'].dtypes


# In[80]:


df['Zone'].dtypes


# In[87]:


df.rename(columns = {'Marital_Status':'Shaadi'}, inplace = True)


# In[89]:


df.columns





# In[90]:


df[['Age','Orders','Amount']].describe()


# In[91]:


df.describe()


# In[92]:


df[['Age','Orders']].describe()


# # Exploratory Data Ananlysis

# In[94]:


ax = sns.countplot(x='Gender',data = df)



# In[95]:


ax = sns.countplot(x='Gender',data = df)

for bars in ax.containers:
    ax.bar_label(bars)


# In[101]:


df.groupby(['Gender'], as_index = False)['Amount'].sum().sort_values(by = 'Amount',ascending = False)


# In[103]:


df.groupby(['Gender'],as_index = False)['Amount'].sum().sort_values(by = 'Amount',ascending = False)


# In[104]:


sales_gen = df.groupby(['Gender'],as_index = False)['Amount'].sum().sort_values(by = 'Amount',ascending = False)
sns.barplot(x = 'Gender',y = 'Amount',data = sales_gen)


# In[105]:


df.columns


# In[107]:


sns.countplot(data = df,x = 'Age Group',hue = 'Gender')


# In[112]:


sales_gen = df.groupby(['Age Group'],as_index = False)['Amount'].sum().sort_values(by = 'Amount',ascending = False)

sns.barplot(x = 'Age Group', y = 'Amount',data = sales_gen)


# In[121]:


sales_state = df.groupby(['State'],as_index = False)['Orders'].sum().sort_values(by = 'Orders',ascending = False).head(10)

sns.set(rc = {'figure.figsize':(15,5)})
sns.barplot(data = sales_state,x = 'State',y = 'Orders')


# In[123]:


sales_state = df.groupby(['State'],as_index = False)['Amount'].sum().sort_values(by = 'Amount',ascending = False).head(10)

sns.set(rc = {'figure.figsize':(10,5)})
sns.barplot(data = sales_state,x = 'State',y = 'Amount')


# In[127]:


ax = sns.countplot(data = df,x = 'Shaadi')

sns.set(rc = {'figure.figsize':(15,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[129]:


df.rename(columns = {'Shaadi':'Marital Status'},inplace = True)


# In[130]:


df.columns


# In[138]:


ax = sns.countplot(data = df,x = 'Marital Status')

sns.set(rc = {'figure.figsize':(7,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[139]:


ax = sns.countplot(data = df,x = 'Marital Status')

sns.set(rc = {'figure.figsize':(15,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[140]:


df.columns


# In[141]:


sns.set(rc = {'figure.figsize':(20,5)})
ax = sns.countplot(data = df,x = 'Occupation')

for bars in ax.containers:
    ax.bar_label(bars)


# In[142]:


sales_state = df.groupby(['Occupation'],as_index = False)['Amount'].sum().sort_values(by = 'Amount',ascending = False)
sns.set(rc = {'figure.figsize':(20,5)})
sns.barplot(data = sales_state,x = 'Occupation',y = 'Amount')


# In[ ]:




