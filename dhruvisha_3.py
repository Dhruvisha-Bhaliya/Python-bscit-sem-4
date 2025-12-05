#!/usr/bin/env python
# coding: utf-8

# In[28]:


# Name: Bhaliya Dhruvisha A.
# class: Sy bsc.it , sem = 4
# Enroll.no: SR22BSIT017
# Date: 16/01/2024
# div: B

# Assignment:3
# AIM: List, tuple, Dictionary and sets

# Implement code of python:
# list1 = ['physics', 'chemistry', 1997, 2000]
# list2 = [1, 2, 3, 4, 5, 6, 7 ]

# 1. Display following items using List:

list1 = ['physics', 'chemistry', 1997, 2000]
print ("list1[0]: ", list1[0])

list2 = [1, 2, 3, 4, 5, 6, 7 ]
print ("list2[1:5]: ", list2[1:5])


# In[25]:


# Example 2: update List items

list = [2000,2001,2002,2003];
print ("Value available at index 2 : ")
print (list[2])

list[2] = 2001;
print ("New value available at index 2 : ")
print (list[2])


# In[26]:


# Example 3:

list1, list2 = [123, 'xyz', 'zara'], [456, 'abc']

print ("First list length : ", len(list1))
print ("Second list length : ", len(list2))


# In[27]:


# Example 4:

list1 = ["a", "b", "c", "d"]
list2 = [25.50, True, -55, 1+2j]

print ("Item at 0th index in list1: ", list1[0])
print ("Item at index 2 in list2: ", list2[1])
print ("Items from index 1 to 2 in list1: ", list1[1:3])
print ("Items from index 0 to 1 in list2: ", list2[0:2])


# In[29]:


#  Example 5

list3 = [1, 2, 3, 4, 5]
print ("Original list ", list3)

list3[2] = 10
print ("List after changing value at index 2: ", list3)


# In[32]:


# Example 6:

list1 = ["a", "b", "c", "d"]
print ("Original list: ", list1)
list2 = ['X','Y', 'Z']
list1[1:3] = list2
print ("List after changing with sublist: ", list1)


# In[42]:


# Example 7:
list1 = ["Rohan", "Physics", 21, 69.75]
print ("Original list ", list1)

list1.insert(2, 'Chemistry')
print ("List after appending: ", list1)

list1.insert(-1, 'Pass')
print ("List after appending: ", list1)


# In[43]:


# Example 8:

list1 = ["a", "b", "c", "d"]
print ("Original list: ", list1)

list1.append('e')
print ("List after appending: ", list1)


# In[44]:


# Example 9:

list1 = ["Rohan", "Physics", 21, 69.75]
print ("Original list: ", list1)

list1.remove("Physics")
print ("List after removing: ", list1)


# In[45]:


# Example 1

tup1 = ('physics', 'chemistry', 1997, 2000)
print ("tup1[0]: ", tup1[0])

tup2 = (1, 2, 3, 4, 5, 6, 7 );
print( "tup2[1:5]: ", tup2[1:5])


# In[50]:


# Example 2

tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');
# Following action is not valid for tuples
# tup1[0] = 100;
# So let's create a new tuple as follows
tup3 = tup1 + tup2;
print (tup3)


# In[74]:


#Example 3
tup = ('physics', 'chemistry', 1997, 2000);
print( tup)
# del (tup)
print ("After deleting tup : ")
print( tup)


# In[80]:


# Self learn python code:

# Q:1 Write a Python program to get the largest number from a list.

list = [1,2,3,4,5,6]
print("Largest element is:", max(list))


# In[90]:


# Q:2 Write a Python program to remove duplicates from a list.

list=[12,15,11,12,8,15,3,3]  
print("The Orijinal list is ",list_value1)  
res=[]  
for i in list:  
    if i not in res:  
        res.append(i)
print("The list after removing duplicates is ",res_list)  


# In[100]:


# Q:3 Write a Python program to select the odd items from a list

list = [11,12,13,14,15,16]
for num in list:
    if num % 2 != 0:
       print(num, end=" ")


# In[99]:


# Q:4 Write a Python program to check if a given string is a Python Keyword or not.
# (Can be implemented with list and keyword library both)

import keyword
print(keyword.iskeyword("xyz"))
print(keyword.iskeyword("for"))
print(keyword.iskeyword("is"))


# In[94]:


# Q:5 Write a python program to display elements of a list in reverse order.

list = [1,2,3,4,5,6]

print(list[::-1])


# In[105]:


# Q:6 Write a Python program to find the length of a tuple.

list = ('physics', 'chemistry', 1997, 2000)
print("The length of tuple is:",len(list))   


# In[110]:


# Q:7 Write a Python program to add member(s) to a set.

thisset = set()
thisset.add('a')
thisset.add('b')
thisset.add('c')
print("Letters are:", thisset)


# In[111]:


# Q:8 Write a Python program to remove item(s) from a given set.

thisset = {1,2,3,4,5,6}
thisset.remove(3)
print(thisset)


# In[118]:


# Q:9 Write a Python program to find the maximum and minimum values in a set.

thisset = {1,2,3,4,5,6}
print("The maximum value of set:",max(thisset))
print("The minimum value of set:",min(thisset))


# In[116]:


# Q:10 Write a Python program to sum all the items in a list.

thisset = [1,2,3,4,5,6,7]
print("Sum of al items:",sum(thisset))


# In[10]:


# Implementation of Dictionary:

# 1. Example 1---


""""subjectandcode={"Physics":42,"Chemistry":43, "Mathematics":41,
"Biology":44,"Computer
Science":83,"Informatics Practices":65,"English":101,"Hindi":2}
subjectandcode["Hindi"]
subjectandcode["Computer Science"]"""

subjectandcode={"Physics":42,"Chemistry":43, "Mathematics":41,
"Biology":44,"Computer Science":83,"Informatics Practices":65,"English":101,"Hindi":2}
print(subjectandcode["Hindi"])
print(subjectandcode["Computer Science"])

# 2. Use of for loop:

for subject in subjectandcode:
    print(subject,":",subjectandcode[subject])
    

# 3. Use of keys( ) and values()

subjectandcode.keys()
subjectandcode.values()


# 4. Subject=list(subjectandcode.keys())

SubjectCode=list(subjectandcode.keys())
print(subject)
SubjectCode=list(subjectandcode.values())
print(SubjectCode)

# 5. subjectandcode["Hindi"]=102

subjectandcode["hindi"]=102
print (subjectandcode["hindi"])

# 6. subjectandcode["Sanskrit"]=122

subjectandcode["sanskrit"]=122
print (subjectandcode["sanskrit"])



# In[11]:


# Example 2:

Employee={"Name":"Bimlendu Kumar", "Department": "Computer Science", "Joining Year":2007}
Employee["Computer Science"]="Bimlendu Kumar";
Employee
Emp1=dict(name="Prakash",Subject="Computer",School="HFC Barauni")
Emp1


# In[14]:


# Example 3: use of following method

"""(a) del <dictionary>[<key>]
(b) <dictionary>.pop(<key>)"""

# Example 3-A:

Subject={'Computer': '083', 'Informatics Practices': '065', 'English': '001'}
del Subject["English"]
Subject

# Example 3-B:

Subject.pop("Computer")
Subject


# In[15]:


# Example 4: check the value is on dictionary or not

emp={'age':25,"Salary":10000,"name":"sanjay"}
"age" in emp
"name" in emp
"basic" in emp
"basic" not in emp


# In[16]:


# Write a python code which check the value
# on dictionary using input any value

dict1={0:"Zero",1:"One",2:"Two",3:"Three",4:"Four",5:"Five"}
# Nested dictionary:
# Example 1:
visitor = {'Name':'Scott','Address':{'hno':'11A/B','City':'Kanpur','PinCode':'208004'}}
visitor
visitor['Name']

