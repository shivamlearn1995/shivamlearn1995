#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing useful library and module to perform linear regression with multiple varibale operations based on hiring data 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


data=pd.read_csv("https://raw.githubusercontent.com/codebasics/py/master/ML/2_linear_reg_multivariate/Exercise/hiring.csv")
data.shape


# In[4]:


data.head()


# In[5]:


data.tail()


# In[6]:


#as we can see that there is NaN value in experuecne and there is NaN or missing value in test_score column
#first treat these column 
data.experience=data.experience.fillna("zero") #missing value of experience i can consider as zero
data


# In[8]:


#We are applying the lineaer regression with multiple varibake or multiple feature 
#the equation is y=m1x1+m2x2+m3x3+m4x4+c here all should have numerical values to find ouput y
#the x1 here experience feature is char or string which is digits in numerical format to convert it we will
#use word2number module 
get_ipython().system('pip install word2number')
from word2number import w2n
data.experience=data.experience.apply(w2n.word_to_num)
data


# In[13]:


#lets treat the tes_score missing values
#here we can take average of test_score to replace the missing values 
#first average the test_score 
import math
averaget_score = math.floor(data['test_score(out of 10)'].mean())
averaget_score


# In[15]:


data['test_score(out of 10)'] = data['test_score(out of 10)'].fillna(averaget_score)
data


# In[17]:


#Lets apply linear regression algorthm using sklearn module
#lets import sklearn module for Linear Regression 
from sklearn.linear_model import LinearRegression
reg=LinearRegression()
reg.fit(data[['experience','test_score(out of 10)','interview_score(out of 10)']],data['salary($)'])


# In[20]:


print("The predicted value based on feature provided ",reg.predict([[2,9,6]]))


# In[21]:


print("The predicted value based on feature provided :",reg.predict([[12,10,10]]))


# In[28]:


#Let's find the coeficient or slope or paramters value 
m1,m2,m3=reg.coef_
print(m1,m2,m3,"Indeed there is a theree slope as we have theree feature so"," here is a value of slope :",reg.coef_)


# In[27]:


#Let's find the intercept values 
c=reg.intercept_


# In[29]:


#Prove the above values using mathematical model
#y=m1x1+m2x2+m3x3+c
x1,x2,x3=2,9,6
y=m1*x1+m2*x2+m3*x3+c
print("The value of prediction based on math model :",y)
print("The  value of predition based on sklearn module:  ",reg.predict([[2,9,6]]))


# # End

# In[ ]:




