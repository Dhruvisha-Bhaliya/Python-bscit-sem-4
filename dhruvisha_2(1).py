#!/usr/bin/env python
# coding: utf-8

# In[73]:


# Name: Bhaliya Dhruvisha A.
# class: Sy bsc.it , sem = 4
# Enroll.no: SR22BSIT017
# Date: 10/01/2024
# div: B

# For Q.1 to 3 Take the following input and generate a given output.

s = 'King Arthur'
print(s[::-1])

snack = "Chocolate ice cream."
print("Updated string:-",snack[10:])

print("Updated string:-",snack[:0]+'vanila',snack[10:19])

str = 'Welcome to the world of Python'
print(str[0]+str[3]+str[6]+str[12]+str[15]+str[18]+str[21]+str[24]+str[27])


# In[72]:


# Q.4 Count and print the occurrence of word “Apple” in following paragraph
# Apple Inc. is an American multinational technology company headquartered in
# Cupertino, California, that designs, develops, and sells consumer electronics, computer
# software, and online services. It is considered one of the Big Four of technology along
# with Amazon, Google, and Facebook.

st='''
Apple Inc is an American multinational technology company headquartered in Cupertino, California, that designs, develops, and sells consumer electronics, computer
software, and online services. It is considered one of the Big Four of technology along
with Amazon, Google, and Facebook.'''
s=st.count("Apple")
print(s)


# In[75]:


# Q.5 Replace word “Apple” with “Google” in above paragraph

txt = "Apple"
x=txt.replace("Apple","Google")
print(x)


# In[92]:


# Q.6 Take string input as below and create a short form of list.
# S = “ Violet Indigo Blue Green Yelllow Orange Red”
# Output: VIBGYO

S = 'Violet Indigo Blue Green Yelllow Orange Red'
x=S.split()
#print(x)
q=[]
for i in x:
    f=i[0]
    q.append(f)
print(''.join(q))


# In[93]:


# Q.7 Switch the case in given string and generate following output.
# var = 'TechBeamers'
# Output : tECHbEAMERS

var = 'TechBeamers'
print(var.swapcase())


# In[95]:


# Q:8 Take string input as below and find the index value of particular word "IOT".
# Input : S1="welcome to the world of IOT"
# Output: 24

S1="welcome to the world of IOT"
print(S1.index('IOT'))


# In[ ]:




