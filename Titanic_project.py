#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# In[12]:


df = pd.read_csv(r'C:\Users\Rukmani\Downloads\titanic.csv')


# In[13]:


df


# In[104]:


df.head(2)


# In[105]:


df.drop('PassengerId',axis = 1,inplace = True)


# In[107]:


df.drop(3)


# In[109]:


df.drop(3,inplace = True)


# In[110]:


df


# In[112]:


df.set_index('Name',inplace = True)


# In[114]:


df.head(2)


# In[115]:


df.reset_index()


# In[119]:


df.head(2)


# In[120]:


df = pd.read_csv(r'C:\Users\Rukmani\Downloads\titanic.csv')


# In[123]:


df


# In[124]:


df.dropna()


# In[4]:


df = pd.read_csv(r'C:\Users\Rukmani\Downloads\titanic.csv')


# In[3]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import plotly. express as px


# In[6]:


df.head(2)


# In[9]:


df.tail(2)


# # shape function it tells to me how many row and columns in dataset 

# In[10]:


df.shape


# In[ ]:


# df.columns it returns the columns name


# In[11]:


df.columns


# # df.dtypes function show the  columns data types

# In[12]:


df.dtypes


# In[ ]:


# df.dtypes == object thats why show the object datatypes only not show the nomerical data types


# In[13]:


df.dtypes == 'Object'


# In[17]:


df.dtypes=='float64'


# In[21]:


df[df.dtypes[df.dtypes=='object'].index]


# In[22]:


df.dtypes=='object'


# In[ ]:


# how to get the numerical columns from the dataset we use the dtypes ==int64 it returns the intger columns


# In[23]:


df[df.dtypes[df.dtypes=='float64'].index]


# In[25]:


df[df.dtypes[df.dtypes=='int64'].index]


# In[ ]:


# describe function returns the mean max count average and describe function apply to on the numerical columns


# In[27]:


df.describe()


# In[30]:


df.describe(include = 'object')


# In[ ]:


# if you want to apply the describe function on seprate columns you can apply


# In[33]:


df[['PassengerId','Age','Pclass']].describe()


# In[ ]:


# df.info function returns the information of the dataset that how many rows and how many columns datatypes


# In[34]:


df.info()


# In[ ]:


# df.isnull function tell how many null values in the dataset


# In[35]:


df.isnull()


# In[ ]:


# df.isnull().sum()it returns the how many total columns null in the dataset 


# In[36]:


df.isnull().sum()


# In[38]:


df.nunique()


# In[39]:


df['PassengerId'].nunique()


# In[40]:


df[['Sex','Fare']].nunique()


# In[44]:


df.describe()


# In[46]:


df[['PassengerId','Survived']].mean()


# In[50]:


df[['PassengerId','Survived']].value_counts()


# In[52]:


df.index


# In[53]:


df[['PassengerId','Pclass']]


# In[54]:


df[['PassengerId','Pclass']].min()


# In[55]:


df[['PassengerId','Pclass']].mode()


# In[56]:


df[['PassengerId','Pclass']].std()


# In[58]:


df.describe()


# In[60]:


df['PassengerId'].max()


# In[63]:


df[['Sex','Age','Parch']].describe()


# In[64]:


df['New']=1


# In[65]:


df.head(3)


# In[ ]:


# df.insert function how to orking here you want to see then you can see


# In[81]:


df.insert(loc = 4,column = 'Food',value = 1)


# In[91]:


df.head(2)


# In[97]:


df.drop('Pclass',axis = 1,inplace = True)


# In[98]:


df.head(2)


# In[100]:


df.drop(3,inplace = True)


# In[101]:


df.head(2)


# In[102]:


df['Name'][0:3]


# In[104]:


df[['Name','Sex']][0:4]


# In[105]:


df[['Name','Sex']][0:10:2]


# In[107]:


v = df['Name'][0:4]


# In[108]:


v


# In[125]:


type(v)


# In[124]:


f = ['a1','a2','a3','a4']


# In[126]:


pd.Series(v,index = f)


# In[127]:


pd.Series(list(v),index = f)


# In[ ]:


# how to change index in data Frame


# In[135]:


c = df['Sex'][0:4]


# In[136]:


c


# In[137]:


type(c)


# In[138]:


g = ['b1','b2','b3','b4']


# In[139]:


pd.Series(c,index = g)


# In[140]:


pd.Series(list(c),index = f)


# In[209]:


df.set_index('Name',inplace =True)


# In[210]:


df.head(3)


# In[219]:


df = pd.read_csv(r'C:\Users\Rukmani\Downloads\titanic.csv')


# In[207]:


df.head(3)


# In[215]:


df.head(3)


# In[217]:


df.dropna(inplace = True)


# In[218]:


df.head(10)


# In[220]:


df.head(10)


# In[224]:


df.fillna('Python',inplace = True)


# In[225]:


df.head(5)


# In[129]:


df.columns


# In[152]:


df.describe(include = 'object')


# In[162]:


df.drop('Fare',axis = 1,inplace =True)


# In[164]:


df.head(3)


# In[166]:


df.dropna(inplace = True)


# In[167]:


df.columns


# In[168]:


df.isnull().sum()


# In[169]:


df.shape


# In[173]:


df.fillna('Hindi',axis = 1,inplace = True)


# In[177]:


df.head(6)


# In[179]:


df[['PassengerId','Pclass','Name']]


# In[180]:


df[['PassengerId','Pclass','Name']].describe()


# In[181]:


df[['PassengerId','Pclass','Name']].sum()


# In[189]:


df[df.dtypes[df.dtypes=='int64'].index]


# In[190]:


df[df.dtypes[df.dtypes=='object'].index]


# In[193]:


df['PassengerId'][0:2]


# In[194]:


df['PassengerId'][3:10:2]


# In[ ]:





# In[4]:


df = pd.read_csv(r'C:\Users\Rukmani\Downloads\titanic.csv')


# In[67]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot
import plotly.express as px


# In[5]:


df.head(5)


# In[6]:


df.isnull().sum()


# In[8]:


df.shape


# In[11]:


df.fillna(method = 'ffill',inplace = True)


# In[12]:


df.shape


# In[13]:


df.head(3)


# In[14]:


df.isna().sum()


# In[16]:


df.fillna(method = 'bfill',inplace = True)


# In[17]:


df.head(5)


# In[20]:


df.rename(columns={'PassengerId':'New_PassengerId'},inplace = True)


# In[22]:


df.head(3)


# In[25]:


df.head(2)


# In[36]:


df.replace(to_replace = 'Name',value = 'New_Name',inplace = True)


# In[38]:


df['Name']


# In[40]:


df.replace(to_replace ='Name',value = 'New_Name',inplace = True)


# In[41]:


df.head(3)


# In[45]:


df.dtypes =='float'


# In[55]:


df['Fare'].dtypes


# In[56]:


df['Fare']=df['Fare'].astype(int)


# In[57]:


df.dtypes


# In[58]:


df[df.dtypes[df.dtypes=='float64'].index]


# In[59]:


df.head(2)


# In[74]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot
import plotly.express as px


# In[81]:


df.head(3)


# In[87]:


sns.lineplot(x = 'PassengerId',y = 'Age',hue = 'Sex',data = df,marker = 'o')



# In[90]:


grouped = df.groupby(['PassengerId','Sex'])
print(grouped)


# In[103]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[116]:


categorical_columns = df.select_dtypes(include =['category','object'])
print(categorical_columns)


# In[160]:


df.head(2)


# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as sns
import seaborn as sns


# In[8]:


df.shape


# In[10]:


df.dtypes


# In[11]:


df.columns


# In[12]:


df.info()


# In[13]:


df.describe()


# In[14]:


df.isnull()


# In[15]:


df.isnull().sum()


# In[16]:


df.nunique()


# In[18]:


df.value_counts()


# In[19]:


df.dtypes =="object"


# In[20]:


df[df.dtypes[df.dtypes=='object'].index]


# In[22]:


df.head(2)


# In[23]:


df['survived'].describe()


# In[24]:


df[['survived','pclass','sex','age']].describe()


# In[27]:


df[['survived','pclass','sex','age']].value_counts


# In[30]:


# df['date']=pd.to_datetime(df['date']).astype('int')


# In[31]:


df.head(2)


# In[35]:


df.drop('sex',axis = 1,inplace = True)


# In[36]:


df.head(2)


# In[37]:


df = sns.load_dataset("titanic")


# In[39]:


df.dropna(inplace = True)


# In[41]:


df.shape


# In[42]:


df.fillna(method = 'bfill',inplace = True)


# In[43]:


df.shape


# In[44]:


df = sns.load_dataset("titanic")


# In[45]:


df.fillna(method = 'bfill',inplace = True)


# In[46]:


df.shape


# In[47]:


df.head(20)


# In[51]:


df['pclass'].value_counts()


# In[52]:


df['pclass'].max()


# In[53]:


df['pclass'].mean()


# In[55]:


df['pclass'].mode()


# In[56]:


df['New_col']=1


# In[60]:


df.columns


# In[64]:


df.head(3)


# In[ ]:


# df.insert(loc=2,column = 'Swati',value = 'food')


# In[71]:


df.rename(columns={'Swati':'New_Swati'},inplace = True)


# In[73]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as sns
import seaborn as sns


# In[88]:


df.head(5)


# In[92]:


df['embarked'].value_counts()


# In[94]:


sns.countplot(x ='embarked',data = df)


# In[95]:


sns.countplot(x ='embarked',data = df,hue = 'sex')


# In[96]:


sns.countplot(x ='pclass',data = df,hue = 'sex')


# In[97]:


df.head(2)


# In[103]:


df['fare'].value_counts()


# In[109]:


df.head(2)


# In[114]:


df['class'].value_counts()


# In[116]:


sns.countplot(x = 'class',data = df,hue = 'sex')


# In[117]:


df.head(4)


# In[119]:


sns.countplot(x = 'survived',data=df,hue ='sex')


# In[121]:


sns.countplot(x = 'survived',data = df,hue = 'class')


# In[143]:


df.head(3)


# In[149]:


sns.displot(x ='who',data =df)


# In[157]:


sns.displot(df['who'],bins = ['man','woman','child'],kde = True,rug = True)
plt.show()


# In[163]:


sns.barplot(x = 'embarked',y = 'survived',data = df)


# In[164]:


sns.barplot(x = 'pclass',y = 'survived',data = df)


# In[168]:


sns.barplot(x = 'sex',y = 'survived',data = df)


# In[169]:


sns.countplot(x = 'sex',data =df)


# In[175]:


order_1 = [3,2,1]
sns.barplot(x = 'pclass',y = 'survived',data = df,
            hue = 'sex',
            order = order_1, hue_order = ['female','male'])


# In[10]:


df.shape


# In[12]:


df.columns


# In[13]:


df.dtypes


# In[14]:


df.head(2)


# In[33]:


sns.countplot(x = 'Pclass',data = df)
plt.title('Count of pclasss')
plt.show()


# In[28]:


df.head(2)


# In[39]:


sns.barplot(x = 'Pclass', y ='PassengerId',data = df,hue = 'Sex')
plt.title('Count of pclasss')
plt.show()


# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[7]:


df = pd.read_csv(r'C:\Users\Rukmani\Downloads\titanic.csv').head(20)


# In[8]:


df.head(5)


# In[9]:


df.shape


# In[12]:


df = pd.read_csv(r'C:\Users\Rukmani\Downloads\titanic.csv')


# In[14]:


df.head(2)


# In[27]:


df.head(2)


# In[32]:


df.head(2)


# In[54]:


sns.displot(x = 'Age',data = df,bins =[0,10,20,30,40,50,60,70,80],kde = True,
           color = 'green')


# In[55]:


df.head(2)


# In[67]:


df['Ticket'].value_counts


# In[68]:


df['Fare']


# In[69]:


df.head(2)


# In[85]:


sns.lineplot(x = 'PassengerId',
             y = 'Age',data = df,hue = 'Sex',
             style = 'Sex',
           markers = ['*','o'])
plt.show()


# In[104]:


sns.scatterplot(x = 'PassengerId',
             y = 'Age',data = df,hue = 'Sex',
               s = 100)
plt.show()   
     


# In[105]:


df.head(2)


# In[114]:


sns.displot(x = 'Age',data = df,hue = 'Sex')


# In[116]:


df.head(2)


# In[120]:


df.head(2)


# In[183]:


sns.histplot(x = 'Age',hue = 'Sex',multiple = 'stack',
           data = df,bins = [0,10,20,30,40,50,60,70,80],kde =True,
           color = 'green')
plt.show()


# In[126]:


df.head(2)


# In[129]:


df['Parch'].value_counts


# In[ ]:





# In[134]:


df = pd.read_csv(r'C:\Users\Rukmani\Downloads\titanic.csv')


# In[135]:


sns.displot(x = 'Fare',
           data = df)


# In[137]:


df.head(2)


# In[147]:


sns.lineplot(x = 'Ticket',y = 'Age',data =df,hue = 'Sex',markers = ['*','o'])
plt.show()


# In[148]:


df.head(2)


# In[149]:


df.head(2)


# In[154]:


sns.barplot(x = 'Survived',y = 'Age',
           data = df,hue = 'Sex')


# In[155]:


df.head(2)


# In[156]:


sns.histplot(x = 'Sex',data = df)


# In[158]:


sns.histplot(x = 'Pclass',data = df)


# In[163]:


sns.countplot(x = 'Survived',hue = 'Sex',
             data = df)


# In[164]:


df.head(2)


# In[166]:


sns.barplot(x = 'Survived',y = 'Age',hue = 'Sex',
           data = df)


# In[167]:


df.head(2)


# In[174]:


sns.histplot(x = 'Age',data = df)
plt.show()


# In[177]:


sns.histplot(df['Fare'], bins = 30,kde = True)
plt.show()


# In[178]:


# Plot age distribution
sns.histplot(df['Age'].dropna(), bins=30, kde=True)
plt.title('Age Distribution')
plt.show()


# In[180]:


# Plot age distribution with hue
sns.histplot(data=df, x='Age', hue='Survived', multiple='stack')
plt.title('Age Distribution by Survival Status')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()


# In[ ]:




