#!/usr/bin/env python
# coding: utf-8

# In[53]:


# Make A pattern Structure using * and using loop method 
for row in range(7):
    for col in range(5):
        if ((col==0 or col==4) and (row>0 and row<7)) or ((row==0 or row==3) and (col>0 and col<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()


# In[5]:


#Make B pattern structure using *
for row in range(7):
    for col in range(5):
        if ((col==0) or (row==0 and row== 6)) or ((row==0 or row==3 or row==6) and (col>0 and col<4)) or ((col==4) and ((row>0 and row<3) or (row>3 and row<6))):
                                                                                                           print("*",end="")
        else:
                                                                                                           print(end=" ")
    print()


# In[37]:


#Make C using "*" pattern 
for row in range(7):
    for col in range(5):
        if ((col==0) and (row>0 and row<6)) or ((row==0 or row==6) and (col>0 and col<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()


# In[42]:


# Make D using "*" pattern 
for row in range(7):
    for col in range(5):
        if (col==0) or ((row==0 or row==6) and (col>0 and col<4)) or ((col==4) and (row>0 and row<6)):
            print("*",end="")
        else:
            print(end=" ")
    print()


# In[43]:


# Make E using "*" pattern  method
for row in range(7):
    for col in range(5):
        if (col==0) or ((row==0 or row==6 or row==3) and (col>0 and col<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()


# In[45]:


#Make G using "*" pattern method 
for row in range(7):
    for col in range(5):
        if ((col==0) and (row>0 and row<6)) or ((row==0 or row==6) and (col>0 and col<3)) or (row==1 and col==3) or ((col==3) and (row>3 and row<6)) or ((row==4) and (col>1 and col<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()
        


# In[47]:


#Make H using "*" pettern method
for row in range(7):
    for col in range(5):
        if (col==0) or (col==4) or ((row==3) and (col>0 and col<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()


# In[49]:


# Make I using "*" pattern method
for row in range(7):
    for col in range(5):
        if (col==2) or (row==0) or (row==6):
            print("*",end="")
        else:
            print(end=" ")
    print()


# In[70]:


# Make J using "*" pattern method
for row in range(7):
    for col in range(7):
        if (row==0) or ((col==3) and (row>0and row<6)) or ((row==6) and (col>0 and col<3)) or ((col==0) and (row>3 and row<6)):
            print("*",end="")
        else:
            print(end=" ")
    print()


# In[71]:


#Make K using "*" pattern method

for row in range(7):
    for col in range(7):
        if (col==0) or (row==0 and col==3) or (row==1 and col==2) or (row==2 and col==1) or (row==4 and col==1) or (row==5 and col==2) or(row==6 and col==3):
            print("*",end="")
        else:
            print(end=" ")
    print()


# In[72]:


#Make F using "*" pattern 
for row in range(7):
    for col in range(5):
        if (col==0) or ((row==0 or row==3) and (col>0 and col<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()


# In[78]:


#Make L using "*" Pattern

for row in range(7):
    for col in range(5):
        if (col==0) or ((row==6) and (col>0 and col<6)):
            print("*",end="")
        else:
            print(end=" ")
    print()


# In[3]:


#for M using "*" Pattern
for row in range(7):
        for col in range(5):
            if (col==0) or (col==4) or (row==2 and col==2) or (row==1 and col==1) or(row==1 and col==3):
                print("*",end="")
            else:
                print(end=" ")
        print()


# In[4]:


#Make N using "*" pattern 
for row in range(7):
    for col in range(7):
        if (col==0) or (col==6) or (row==1 and col==1) or (row==2 and col==2) or (row==3 and col==3) or (row==4 and col==4) or (row==5 and col==5):
            print("*",end="")
        else:
            print(end=" ")
    print()


# In[9]:


#Make o using "*" pattern 
for row in range(5):
    for col in range(5):
        if (col==0 and (row>0 and row<4)) or (col==4 and (row>0 and row<4)) or ((row==0) and (col>0 and col<4 )) or ((row==4) and (col>0 and col<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()


# In[12]:


#Make P using "*" Pattern 
for row in range(7):
    for col in range(5):
        if (col==0) or ((row==0 or row==4) and (col>0 and col<4)) or ((row>0 and row<4) and (col==4)):
                        print("*",end="")
        else:
                        print(end=" ")
    print()


# In[13]:


#Make Q using "*" pattern 
for row in range(7):
    for col in range(6):
        if (col==0 and (row>0 and row<4)) or (col==4 and (row>0 and row<4)) or ((row==0) and (col>0 and col<4 )) or ((row==4) and (col>0 and col<4)) or(row==3 and col==2)or (row==5 and col==4) or(row==6 and col==6):
            print("*",end="")
        else:
            print(end=" ")
    print()


# In[14]:


#Make R using "*" pattern 
for row in range(9):
    for col in range(5):
        if (col==0) or ((row==0 or row==4) and (col>0 and col<4)) or ((row>0 and row<4) and (col==4)) or (row==5 and col==1) or(row==6 and col==2)or (row==7 and col==3)or (row==8 and col==4):
                        print("*",end="")
        else:
                        print(end=" ")
    print()


# In[22]:


# Make S using "*" pattern
for row in range(11):
    for col in range(5):
        if ((col==0 or col==4) and (row>0 and row<5)) or ((col==0 or col==4)and (row>6 and row<10)) or ((row==0 or row==10) and(col>0 and col<4))or ((col==1 and row==5)) or(row==6 and col==2):
            print("*",end="")
        else:
            print(end=" ")
    print()


# In[27]:


#Make T using "*" pattern 
for row in range(5):
    for col in range(7):
        if (col==3) or (row==0):
            print("*",end="")
        else:
            print(end=" ")
    print()


# In[28]:


# Make U using "*" pattern 
for row in range(5):
    for col in range(5):
        if (col==0 and (row>0 and row<4)) or (col==4 and (row>0 and row<4)) or ((row==4) and (col>0 and col<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()


# In[44]:


# Make V using "*" pattern 
for row in range(4):
    for col in range(13):
        if ((row==0) and (col==0 or col==6)) or ((row==1) and (col==1 or col==5)) or ((row==2) and (col==2 or col==4)) or ((row==3) and (col==3)):
            print("*",end="")
        else:
            print(end=" ")
    print()


# In[43]:


#Make W using * pattern 
for row in range(4):
    for col in range(13):
        if ((row==0) and (col==0 or col==6 or col==12)) or ((row==1) and (col==1 or col==5 or col==7 or col==11)) or ((row==2) and (col==2 or col==4 or col==8 or col==10)) or ((row==3) and (col==3 or col==9)):
            print("*",end="")
        else:
            print(end=" ")
    print()


# In[46]:


# Make X using * pettern 
for row in range(5):
    for col in range(5):
        if ((row==0) and (col==0 or col==4)) or ((row==1) and (col==1 or col==3)) or ((row==4) and (col==0 or col==4)) or (row==2 and col==2) or ((row==3) and(col==1 or col==3)):
            print("*",end="")
        else:
            print(end=" ")
    print()


# In[51]:


# Make Y using * pattern 
for row in range(5):
    for col in range(5):
        if ((row>1 and row<5) and (col==2)) or ((row==0) and (col==0 or col==4)) or ((row==1) and (col==1 or col==3) ):
            print("*",end="")
        else:
            print(end=" ")
    print()


# In[52]:


# Make Z using * pattern 
for row in range(5):
    for col in range(5):
        if (row==0) or (row==4) or (row==1 and col==3) or (row==2 and col==2) or (row==3 and col==1):
            print("*",end="")
        else:
            print(end=" ")
    print()


# In[ ]:




