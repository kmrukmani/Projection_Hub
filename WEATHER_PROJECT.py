#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd 


# In[3]:


data = pd.read_csv(r"C:\Users\Rukmani\Downloads\1. Weather Data.csv")


# In[4]:


# head function  returns the top 5 rows() it show by default five rows()
data.head()


# In[5]:


data.head(10)


# In[6]:


#Shape function it shows the how many rows and columns present in the data
#data.shape
# it applies thats whay i can get the eaisly how many rows and columns
# it cant appaly in round bracket
data.shape


# In[7]:


# COLUMNS FUNCTION it shows the each name of columns
# i have applied see the what are the name of each column
data.columns


# In[10]:


#values counts it show the how many values in the present data
# values.counts it is count the values present the data it can be applied column and data frame
data.value_counts()


# In[23]:


data.index


# In[ ]:


# This attribute  provide the index of the data


# In[24]:


data.dtypes


# In[29]:


data.nunique()


# In[31]:


data.Weather.unique()


# In[32]:


data.nunique()


# In[36]:


data.Weather.nunique()


# In[39]:


data.isnull()


# In[47]:


data.isnull().sum()


# In[48]:


data.describe()


# In[49]:


data.info()


# In[51]:


data.describe(include = "object")


# In[53]:


data.describe(include = "int")


# In[54]:


data.describe(include = "float")


# In[55]:


data.head(2)


# In[61]:


data['Weather'].unique()


# In[62]:


data.head(3)


# In[ ]:


# It can be applies on single column and i shows the total number of unique from the dataframe
#it shows the total n of unique in each column


# In[63]:


data['Wind Speed_km/h'].unique


# In[64]:


data.nunique()


# In[66]:


data['Wind Speed_km/h'].nunique()


# In[70]:


data['Wind Speed_km/h'].value_counts()


# In[72]:


# count function it shows the no of non values nun null values
#.count()it can be applied on single column as well as on whole data frame
data.count()


# In[73]:


data.isnull().sum()


# In[74]:


data.isnull()


# In[75]:


#value_counts() in a column,it shows the unique value with their count it can be applied on 
# single column only()
data['Weather'].value_counts()


# In[76]:


data.head()


# In[77]:


data['Wind Speed_km/h'].value_counts()


# In[78]:


# Info commond the  provides the  basic information about the dataframe()
data.info()


# # Exeploratory data
# 

# In[81]:


# Find the all unique numbers 'Wind Speed ' values in data
data.nunique()
# This first method how to find unique numbers 'wind speed'


# In[83]:


# This is Second STEP HOW TO Access the unique numbers from the 'wind speed'
data['Wind Speed_km/h'].unique()


# In[84]:


data['Wind Speed_km/h'].nunique()


# In[ ]:


# Find the Numbers of times when the "Weather is Exetly clear"
# There are three types of to find the numbers of times

# Value_counts()
# filtering()
# groupby()


# In[88]:


# First using value_counts()
data.Weather.value_counts()


# In[89]:


data['Weather'].value_counts()


# In[95]:


data[data.Weather == 'Clear']


# In[96]:


data.Weather == 'clear'


# In[99]:


# Groupby commond
# data.head(2)
data.groupby('Weather').get_group('Clear')


# In[100]:


#Find the Number of times when the 'wind Speed was cexetly 4 km/h'
data.head()


# In[104]:


data[data['Wind Speed_km/h'] == 4]


# In[105]:


#Find out all the Null Values in the data
data.isnull().sum()


# In[107]:


data.head()


# In[109]:


data.rename(columns={'Weather':'Weather Condition'},inplace = True)


# In[110]:


data.head()


# In[112]:


data.rename(columns = {'Weather Condition':'Weather'},inplace = True)


# In[113]:


data.head(10)


# In[118]:


data.rename(columns = {'Weather ':'Weather Condition'},inplace = True)


# In[119]:


data.head(2)


# In[121]:


# WHAT IS THE MEAN 'VISIBILITY'
data.head(2)


# In[122]:


data.Visibility_km.mean()


# In[128]:


data.head(2)


# In[130]:


data.describe()


# In[131]:


data.Press_kPa.std()


# In[132]:


data.head(2)


# In[133]:


data['Rel Hum_%'].var()


# In[137]:


data['Weather'].value_counts()


# In[138]:


data['Weather']=='Snow'


# In[140]:


data[data['Weather']=='Snow']


# In[142]:


data[data['Weather'].str.contains('Snow')]


# In[143]:


data[(data['Wind Speed_km/h'] >24)&(data['Visibility_km']==25)]


# In[145]:


# What is the mean value of each column against each 'Wearther condition'
data.groupby('Weather').mean()


# In[146]:


data.head(2)


# In[147]:


# What is maximum and minimum value of each column against
# each weather condition
data.groupby('Weather').min()


# In[148]:


data.groupby('Weather').max()


# In[149]:


data.head(2)


# In[151]:


data[data['Weather']=='Fog']


# In[ ]:




