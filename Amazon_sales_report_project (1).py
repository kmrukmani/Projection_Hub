#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# import libraries


# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[7]:


data = pd.read_csv("E:\Python_Amazon_Sales_Analysis-main\Python_Amazon_Sales_Analysis-main\Amazon Sale Report.csv")


# In[8]:


data.info()


# In[9]:


# It returns the top  five of rows from dataset

data.head() 


# In[11]:


# It returns the bottom five of rows from dataset

data.tail()


# In[13]:


# check the null values
# It returns the true and false values from dataset 
data.isnull()


# In[18]:


# if want to check the total null values we use data.isnul().sum()
pd.isnull(data).sum()
whatever you can use
data.isnull().sum()


# In[30]:


data = data.drop(columns = ['New','PendingS'])


# In[31]:


data.isnull().sum()


# In[33]:


# It returns the total number of rows and columns represent in your dataset and
# data.shape function tells that how many rows and columns avialables
data.shape 


# In[36]:


# remove\ drop Null values
data.dropna(inplace = True)


# In[38]:


data.shape


# In[39]:


data.isnull().sum()


# In[41]:


data.info()


# In[43]:


data.head(3)


# In[45]:


# change  data type: when i will take [] bracket when we types column name
# when we have to change data type i will use this method
data['ship-postal-code'] = data['ship-postal-code'].astype('int')


# In[47]:


# check  data type change or  not
# after changing the data type we should check data type change or not

data['ship-postal-code'].dtype


# In[49]:


data['Date'] = pd.to_datetime(data['Date'])


# In[50]:


data['Date'].dtype


# In[51]:


# # suppose if you want see the standard devition and mean max avg sum 
# you can use the describe functions
data.describe()


# In[52]:


# describe our data with objects datatypes

data.describe(include  = 'object')


# In[54]:


# describe for specific columns 
data[['Qty','Amount']].describe()  


# In[56]:


data.head()


# In[58]:


ax = sns.countplot(x = 'Size',data = data)

# checking for data labels
for bars in ax.containers:
    ax.bar_label(bars)


# # Most of the people buy  M - Size

# In[63]:


# courier staus
plt.figure(figsize =(10,6))
sns.countplot(data = data,x ='Courier Status',hue = 'Status' )
plt.show()


# # Majority to the orders are shipped through the courier

# In[65]:


data.head()


# In[67]:


data.info()


# In[72]:


data['Category'] = data['Category'].astype(str)
c_d = data['Category']
plt.figure(figsize=(10,6))
plt.hist(c_d,bins=30,edgecolor='black',color='yellow')
plt.xticks(rotation = 90)
plt.show


# # Most of the buyers are T-shirt

# In[77]:


# check b2b data
check_B2B = data['B2B'].value_counts()

# create pie chart
plt.pie(check_B2B,labels = check_B2B.index,autopct = '%1.1f%%')
plt.show()


# # Maximum 99.2% buyers are retailers and 0.8% are wholesalers

# In[95]:


plt.scatter(data['Category'],data['Size'])
plt.xlabel('Category')
plt.ylabel('Size')
plt.title('Available Size')
plt.show()


# In[103]:


top10_state = data['ship-state'].value_counts().head(10) # For Top 10 states

plt.figure(figsize =(12,6))
sns.countplot(data = data[data['ship-state'].isin(top10_state.index)],x ='ship-state')

plt.xlabel('State',fontsize = 15)
plt.ylabel('Orders_count',fontsize = 15)
plt.title('Distribution of State',fontsize = 15)
plt.xticks(rotation = 90)
plt.show()


# # Most of the buyers are Maharashtra state

# In[ ]:




