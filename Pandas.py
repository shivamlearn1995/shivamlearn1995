#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Pandas used for python data analytics. 
#types of data :- 1D, 2D, 3D. 
#3D data are image 
#data dimensions 
#(i) 1-D series 
#(ii) 2-D Dataframes
#(iii) 3-D Pannel 
# data sources 
#(i) uci-ml repository
#(ii) kaggle.co
#(iii) data.gov.in
#(iv) github.com
#bit.ly


# In[2]:


#data extensions
#.json
#.csv
#.sql
#.pickle
#.arff
#.html
#.tsv


# In[3]:


import pandas as pd
dt=pd.read_csv("https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/imdb_1000.csv")


# In[4]:


#shape of the data ( means rows and columns of the data)


# In[5]:


dt.shape


# In[6]:


# ffor knowing columns of the data


# In[7]:


dt.columns


# In[8]:


# to view data from top head, by default it will show the first five data


# In[9]:


dt.head()


# In[10]:


type(dt)


# In[11]:


#to view first 10 data sets 


# In[12]:


dt.head(10)


# In[13]:


#what we can do with this data ?
#1. we can give brief inisights of genre


# In[14]:


# we have to give basic graph to make data usefu;


# In[15]:


dt.tail()


# In[16]:


#filter on data


# In[17]:


dt['duration']


# In[18]:


dt.duration


# In[19]:


# if we want to get the movie greater than 3 hrs 


# In[20]:


x=dt.duration>200


# In[21]:


dt[x]


# In[22]:


dt[dt.duration>200]


# In[23]:


# if we want to extract the data of movies whose duration is 200 and genre is drama


# In[24]:


dt[(dt.duration>200)&(dt.genre=='Drama')]


# In[25]:


#if we want to extract many features or relations in one go then code should be 


# In[26]:


dt[(dt.duration>200)&(dt.genre.isin(['Drama','Action','Crime']))]


# In[27]:


#if we want to extract actors list then, and the movies should be 
#bollywood as clients want to know the bollywood data.
#we can search Indian actors list to know the bollywoood movie


# In[28]:


dt[dt.actors_list.str.contains("Khan")]


# In[29]:


#if we want to know how many unique genre are there.


# In[30]:


dt.genre.unique()


# In[31]:


#if we want to no. of unique genre


# In[32]:


dt.genre.unique()


# In[33]:


#if we want to know how many drama then 


# In[34]:


dt.genre.value_counts()


# In[35]:


# if we want to understand the relationship between movie genre and no. of 
#movies,then we will use visualization by following code


# In[36]:


dt.genre.value_counts().plot(kind='bar')


# In[37]:


#to know the statistical interpretation we will  use following code


# In[38]:


dt.duration.describe()


# In[39]:


#to plot describe in the graph


# In[40]:


get_ipython().run_line_magic('matplotlib', 'notebook')
dt.groupby("genre").duration.describe().plot(kind='bar')


# In[41]:


#pandas is 17 different library


# In[42]:


#data which has higher variance is continious data temperature 


# In[43]:


dt.genre.describe()


# In[44]:


#if you want to check move list of Amir Khan 


# In[48]:


dt[dt.actors_list.str.contains("Khan")]


# In[49]:


#movie list of Sanjay dutt


# In[50]:


dt[dt.actors_list.str.contains("Dutt")]


# In[51]:


#unique value of genre


# In[52]:


dt.genre.unique()


# In[53]:


#count of unique genre


# In[54]:


dt.genre.value_counts()


# In[55]:


#To plot vthe graph


# In[56]:


dt.genre.value_counts().plot(kind='bar')


# In[57]:


#Represent data values into percentages


# In[59]:


round(dt.genre.value_counts(normalize=True)*100,2)


# In[60]:


#sorting of data based on parameters


# In[61]:


dt.sort_values('duration').head(10)


# In[62]:


#sorting based on duration and ratings 
#Primary sorting----> duration
#secondary sorting----> ratings 


# In[64]:


dt.sort_values(['duration','star_rating']).head(20)


# In[65]:


#sorting of duration,ratings and title.


# In[66]:


dt.sort_values(['duration','star_rating','title']).head(20)


# In[67]:


#To list data in ascending and descending order.


# In[68]:


dt.sort_values(['duration','star_rating','title'],ascending=[True,False,True]).head(20)


# In[69]:


#Data in stastical view altogether 


# In[71]:


dt.duration.agg(['min','max','mean','std','median']) #numeric data 


# In[72]:


#to get the statistical view of non-numerical data


# In[73]:


dt.genre.describe()


# In[74]:


#For multiple column statistical result


# In[75]:


dt[['duration','star_rating']].describe()


# In[76]:


#When there is numeric and non-numeric data on describe operation.


# In[78]:


dt[['genre','duration']].describe() #Non-numeric data is skipped 


# In[79]:


dt.describe().plot(kind='bar')


# In[80]:


for i in dt.genre.unique():
    print(dt[dt.genre==i].describe(),i)


# In[81]:


#to describe the databased on group of data.


# In[82]:


dt.groupby('genre').describe()


# # Indexing and slicing Methods

# In[84]:


#loc 
#iloc
#se_index
#reset_index


# In[88]:


dt1=pd.read_csv("https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/drinks.csv")


# In[89]:


dt1.head()


# In[90]:


# Finding the indexes 


# In[91]:


dt1.index


# In[92]:


#dt1[0] will not work


# In[93]:


dt[0]


# In[94]:


#loc is a index based indexer, by using this we can perform the slicing, indexing on our dataframe


# In[95]:


#we can change the data in the row/column, we can create a new row column
#loc[row_indexer,col_indexer]


# In[96]:


dt1[0:1] # for accessing first index elements ""


# In[98]:


dt1.loc[0,'beer_servings']


# In[99]:


dt1.head()


# In[100]:


#modify column using loc


# In[101]:


dt1.loc[0,'beer_servings']+=34
dt1.head()


# In[102]:


#If you want access, the multiple rows then following programs


# In[103]:


dt1.loc[0:5,['beer_servings','spirit_servings']]


# In[104]:


#for selected rows operation


# In[105]:


dt1.loc[[0,3,45,72,78],['beer_servings','continent']]


# In[106]:


#iloc is used for positional indexing and slicing of the data by using iloc we can manipulate the values.
#but we cannot create new row/column 
#iloc[row_indexer,column_indexer]


# In[107]:


dt1.iloc[0,1]


# In[108]:


#iloc cannot have substring in index 


# In[109]:


dt1.iloc[0,"beer_servings"]


# In[110]:


#iloc will work as pure indexing.


# In[111]:


dt1.iloc[0:5]


# In[112]:


#for selected rows


# In[113]:


dt1.iloc[[0,4,12,56,79]]


# In[114]:


#select bot rows and columns 


# In[115]:


dt1.iloc[[0,4,12,56,79],[0,1,2,3]]


# In[116]:


#iloc method with selected rows with column slicing


# In[117]:


dt1.iloc[[0,4,12,56,79],0:6]


# In[118]:


#filter based on general method vs iloc 


# In[119]:


dt1.iloc[77]


# In[121]:


dt1[dt1.country=='India']


# In[122]:


#To add new column in the table we can use assignment operations just like list


# In[123]:


dt1.loc[193]=['New',10,10,10,10,"Artantica"]


# In[124]:


dt1.tail()


# In[125]:


dt1.set_index("country")
dt1.head()


# # set_index

# In[126]:


##to store locally we use set_index


# #set_index:-It is used to make any column as an index of our data. It will return a new data with the given 
# #column as its index. If we want the current data index to be replace by the given column then we have to use 
# #the agrugment "inplace=True"

# In[136]:


dt1.set_index("country",inplace=True)


# In[137]:


dt1.loc['India']


# In[138]:


dt1.iloc[77]


# In[140]:


dt1.loc[77] #it will give the error


# # reset_index

# #if we want to create index as a new column then we can use reset_index tyo make changes locally we can 
# #use the keyword argument "inplace=True".

# In[141]:


dt1.reset_index()


# In[142]:


dt1.head()


# In[143]:


dt1.reset_index(inplace=True)


# In[144]:


dt1.head()


# In[145]:


#if we by mistake run reset_index 2-3 times then data will add in the table in that case


# # Drop

# In[146]:


#by using  drop we can remove any row/column from our data. If we are removing a row or list of row 
#we need to use inplce=True 


# In[147]:


#to make changes locally, but incase of columns ar list of columns we have to use a keyword argument
#as axis =1 to remove the columns and for changes locally we have to use inplace=True


# In[148]:


dt1.drop(0) #it will remove all the values of afghanistan


# In[149]:


#to remove the column


# In[153]:


dt1.drop('country',axis=1)


# In[154]:


dt1.head()


# In[155]:


#to change locally


# In[156]:


dt1.drop('country',axis=1,inplace=True)


# In[157]:


dt1.head()


# # Data type conversions

# In[158]:


#astype
#pd.to_numeric
#astype.cat.codes
#astype and pd.to_numeric by using these methods we can convert the data by specifying the data types like 'i'
#for integer 'f' for float 'c' for complex, 'o' for object(string).


# In[159]:


dt2=pd.read_csv("https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/chipotle.tsv") 
#will give an error cause the data is tsv(tab seperated value)


# In[160]:


dt2=pd.read_table("https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/chipotle.tsv")


# In[161]:


dt2.head()


# In[162]:


#Carve out the content which has chicken somewhere in between 


# In[165]:


dt2[dt2.item_name.str.contains("Chicken")]


# In[166]:


#item_price of item_name which contains Chicken


# In[167]:


dt2[dt2.item_name.str.contains("Chicken")].item_price


# In[169]:


dt2[dt2.item_name.str.contains("Chicken")].item_price.describe()


# In[170]:


#to convert into float data type (dtype)


# In[171]:


dt2.item_price.str.lstrip("$").astype(dtype='f')


# In[172]:


#or can be written as 


# In[173]:


pd.to_numeric(dt2.item_price.str.lstrip("$"))


# In[174]:


#converting name(here it means character or strings ) to in the form of number


# In[175]:


dt2.item_name.astype(dtype='category').cat.codes


# # Missing Values types

# In[176]:


#isnull
#notnull
#dropna
#fillna
#you can manipulate missing values based on above values methods 


# In[177]:


dt3=pd.read_csv("https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv")


# In[178]:


dt3.head()


# In[179]:


#NaN values in datasets denotes to null values 


# In[180]:


dt3.isnull().sum()


# In[181]:


#to know how many data are there in the file 


# In[182]:


dt3.notnull().sum()


# In[186]:


dt3.dropna().shape 


# In[185]:


#to drop off all values which contains NULL


# In[187]:


dt3.dropna(how='all')


# In[188]:


#drop if any value has NaN


# In[189]:


dt3.dropna(how='any').shape


# In[190]:


#columnwise operation
#if axis=1 use, then it is to be understood that column is used.(applicable to all operations)


# In[191]:


dt3.dropna(axis=1).shape


# In[193]:


dt3.dropna(how='any',axis=1).shape


# In[194]:


#to replace message where value not found in the column 


# In[195]:


dt3.fillna("NoValueFound")


# In[196]:


#memory management
#info
#memory_usage


# In[197]:


dt3.info()


# In[198]:


#column+content data usage 


# In[199]:


dt3.info(memory_usage='deep')


# In[200]:


dt3.memory_usage()


# In[201]:


dt3.memory_usage().sum()


# In[ ]:




