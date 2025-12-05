#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Assignment-7:

# Aim: Pandas Series and Dataframe

# 1. Write a Pandas program to create and display a one-dimensional
# array-like object containing an array of data using Pandas module.

import pandas as pd
ds = pd.Series([2, 4, 6, 8, 10])
print(ds)


# In[2]:


# 2. Write a Pandas program to convert a Panda module Series to Python list
# and its type. [Hint : Use of tolist()method]

import pandas as pd
ds = pd.Series([2, 4, 6, 8, 10])
print("Pandas Series and type")
print(ds)
print(type(ds))
print("Convert Pandas Series to Python list")
print(ds.tolist())
print(type(ds.tolist()))


# In[3]:


"""
3. Write a Pandas program to add, subtract, multiple and divide two Pandas
Series.
Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 9]
Hint: ds = ds1 + ds2
ds = ds1 - ds2
ds = ds1 * ds2
ds = ds1 / ds2
"""

import pandas as pd
ds1 = pd.Series([2, 4, 6, 8, 10])
ds2 = pd.Series([1, 3, 5, 7, 9])
ds = ds1 + ds2
print("Add two Series:")
print(ds)
print("Subtract two Series:")
ds = ds1 - ds2
print(ds)
print("Multiply two Series:")
ds = ds1 * ds2
print(ds)
print("Divide Series1 by Series2:")
ds = ds1 / ds2
print(ds)


# In[4]:


"""
4. Write a Pandas program to compare the elements of the two Pandas
Series. Take sample as following:
Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 10]
Hints:
print("Compare the elements of the said Series:")
print("Equals:")
print(ds1 == ds2)
print("Greater than:")
print(ds1 > ds2)
print("Less than:")
print(ds1 < ds2)
"""

import pandas as pd
ds1 = pd.Series([2, 4, 6, 8, 10])
ds2 = pd.Series([1, 3, 5, 7, 10])
print("Series1:")
print(ds1)
print("Series2:")
print(ds2)
print("Compare the elements of the said Series:")
print("Equals:")
print(ds1 == ds2)
print("Greater than:")
print(ds1 > ds2)
print("Less than:")
print(ds1 < ds2)


# In[5]:


"""
5. Write a Pandas program to convert a dictionary to a Pandas series. [Hint
Use dictionary object and convert it into Series]
Sample Series:
Original dictionary:
{'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
Converted series:
a 100
b 200
c 300
d 400
e 800
dtype: int64
"""

import pandas as pd
d1 = {'a': 100, 'b': 200, 'c':300, 'd':400, 'e':800}
print("Original dictionary:")
print(d1)
new_series = pd.Series(d1)
print("Converted series:")
print(new_series)


# In[6]:


"""
6. Write a Pandas program to convert a NumPy array to a Pandas
series.[Hint: create numpy array and convert it into Series]
Sample Series:
NumPy array:
[10 20 30 40 50]
Converted Pandas series:
0 10
1 20
2 30
3 40
4 50
dtype: int64
"""

import numpy as np
import pandas as pd
np_array = np.array([10, 20, 30, 40, 50])
print("NumPy array:")
print(np_array)
new_series = pd.Series(np_array)
print("Converted Pandas series:")
print(new_series)


# In[7]:


"""
7. Write a Pandas program to change the data type of given a column or a
Series. [Hint: use to_numeric() method]
Sample Series:
Original Data Series:
0 100
1 200
2 python
3 300.12
4 400
dtype: object
Change the said data type to numeric:
0 100.00
1 200.00
2 NaN
3 300.12
4 400.00
dtype: float64
"""

import pandas as pd
s1 = pd.Series(['100', '200', 'python', '300.12', '400'])
print("Original Data Series:")
print(s1)
print("Change the said data type to numeric:")
s2 = pd.to_numeric(s1, errors='coerce')
print(s2)


# In[8]:


"""
8. Write a Pandas program to select the specified columns and rows from a
given data frame.
Sample Python dictionary data and list labels:
Select 'name' and 'score' columns in rows 1, 3, 5, 6 from the following data
frame.
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily',
'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
Expected Output:
Select specific columns and rows:
score qualify
b 9.0 no
d NaN no
f 20.0 yes
g 14.5 yes
"""

import pandas as pd
import numpy as np

exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data , index=labels)
print("Select specific columns and rows:")
print(df.iloc[[1, 3, 5, 6], [1, 3]])


# In[10]:


"""
9. Write a Pandas program to select the rows where the number of attempts
in the examination is greater than 2.
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily',
'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
Expected Output:
Number of attempts in the examination is greater than 2:
name score attempts qualify
b Dima 9.0 3 no
d James NaN 3 no
f Michael 20.0 3 yes
"""

import pandas as pd
import numpy as np

exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts' : [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data , index=labels)
print("Number of attempts in the examination is greater than 2:")
print(df[df['attempts'] > 2])


# In[11]:


"""
10. Write a Pandas program to count the number of rows and columns of a
DataFrame.
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily',
'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
Expected Output:
Number of Rows: 10
Number of Columns: 4
"""

import pandas as pd
import numpy as np
exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data , index=labels)
total_rows=len(df.axes[0])
total_cols=len(df.axes[1])
print("Number of Rows: "+str(total_rows))
print("Number of Columns: "+str(total_cols))


# In[12]:


"""
11. Write a Pandas program to select the rows where the score is missing,
i.e. is NaN.
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily',
'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
Expected Output:
Rows where score is missing:
attempts name qualify score
d 3 James no NaN
h 1 Laura no NaN
"""

import pandas as pd
import numpy as np
exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data , index=labels)
print("Rows where score is missing:")
print(df[df['score'].isnull()])


# In[13]:


"""
Advanced:
1. Write a Pandas program to display the default index and set a column
as an Index in a given dataframe.
Test Data:
0 s001 V Alberto Franco 15/05/2002 35 street1 t1
1 s002 V Gino Mcneill 17/05/2002 32 street2 t2
2 s003 VI Ryan Parkes 16/02/1999 33 street3 t3
3 s001 VI Eesha Hinton 25/09/1998 30 street1 t4
4 s002 V Gino Mcneill 11/05/2002 31 street2 t5
5 s004 VI David Parkes 15/09/1997 32 street4 t6
Code:
import pandas as pd
df = pd.DataFrame({
'school_code': ['s001','s002','s003','s001','s002','s004'],
'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino
Mcneill', 'David Parkes'],
'date_Of_Birth':
['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
'weight': [35, 32, 33, 30, 31, 32],
'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4'],
't_id':['t1', 't2', 't3', 't4', 't5', 't6']})
print("Default Index:")
print(df.head(10))
print("\nschool_code as new Index:")
df1 = df.set_index('school_code')
print(df1)
print("\nt_id as new Index:")
df2 = df.set_index('t_id')
print(df2)
"""

import pandas as pd
df = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_Of_Birth': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4'],
    't_id':['t1', 't2', 't3', 't4', 't5', 't6']})
print("Default Index:")
print(df.head(10))
print("\nt_id as new Index:")
df1 = df.set_index('t_id')
print(df1)
print("\nReset the index:")
df2 = df1.reset_index(inplace=False)
print(df2)


# In[14]:


"""
Q-2: Write a Pandas program to create a multi Index frame using two columns
and using an Index and a column.
Test Data:
0 s001 V Alberto Franco 15/05/2002 35 street1 t1
1 s002 V Gino Mcneill 17/05/2002 32 street2 t2
2 s003 VI Ryan Parkes 16/02/1999 33 street3 t3
3 s001 VI Eesha Hinton 25/09/1998 30 street1 t4
4 s002 V Gino Mcneill 11/05/2002 31 street2 t5
5 s004 VI David Parkes 15/09/1997 32 street4 t6
"""

import pandas as pd
df = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_Of_Birth': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4'],
    't_id':['t1', 't2', 't3', 't4', 't5', 't6']})
print("Original DataFrame:")
print(df)
print("\nMultiIndex using columns 't_id' and ‘school_code’:")
df1 = df.set_index(['t_id', 'school_code'])
print(df1)
print("\nMultiIndex using an Index and a column:")
df2 = df.set_index([pd.Index([0, 1, 2, 3, 4, 5]), 't_id'])
print(df2)


# In[15]:


"""
3. Write a Pandas program to display the default index and set a column as an Index in a
given dataframe and then reset the index.
Test Data:
0 s001 V Alberto Franco 15/05/2002 35 street1 t1
1 s002 V Gino Mcneill 17/05/2002 32 street2 t2
2 s003 VI Ryan Parkes 16/02/1999 33 street3 t3
3 s001 VI Eesha Hinton 25/09/1998 30 street1 t4
4 s002 V Gino Mcneill 11/05/2002 31 street2 t5
5 s004 VI David Parkes 15/09/1997 32 street4 t6
"""

import pandas as pd
df = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_Of_Birth': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4'],
    't_id':['t1', 't2', 't3', 't4', 't5', 't6']})
print("Default Index:")
print(df.head(10))
print("\nt_id as new Index:")
df1 = df.set_index('t_id')
print(df1)
print("\nReset the index:")
df2 = df1.reset_index(inplace=False)
print(df2)


# In[16]:


"""
4. Write a Pandas program to create an index labels by using 64-bit integers, using
floating-point numbers in a given dataframe.
Test Data:
0 s001 V Alberto Franco 15/05/2002 35 street1 t1
1 s002 V Gino Mcneill 17/05/2002 32 street2 t2
2 s003 VI Ryan Parkes 16/02/1999 33 street3 t3
3 s001 VI Eesha Hinton 25/09/1998 30 street1 t4
4 s002 V Gino Mcneill 11/05/2002 31 street2 t5
5 s004 VI David Parkes 15/09/1997 32 street4 t6
"""

import pandas as pd
print("Create an Int64Index:")
df_i64 = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_Of_Birth': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']},
    index=[1, 2, 3, 4, 5, 6])
print(df_i64)
print("\nView the Index:")
print(df_i64.index)

print("\nFloating-point labels using Float64Index:")
df_f64 = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_Of_Birth ': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']},
    index=[.1, .2, .3, .4, .5, .6])
print(df_f64)
print("\nView the Index:")
print(df_f64.index)


# In[17]:


# 5. Write a Pandas program to create a DataFrame using intervals as an index

import pandas as pd
print("Create an Interval Index using IntervalIndex.from_breaks:")
df_interval = pd.DataFrame({"X":[1, 2, 3, 4, 5, 6, 7]},
                            index = pd.IntervalIndex.from_breaks(
                            [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3, 3.5]))    
print(df_interval)
print(df_interval.index)

print("\nCreate an Interval Index using IntervalIndex.from_tuples:")
df_interval = pd.DataFrame({"X":[1, 2, 3, 4, 5, 6, 7]},             
                            index = pd.IntervalIndex.from_tuples(
                            [(0, .5), (.5, 1), (1, 1.5), (1.5, 2), (2, 2.5), (2.5, 3), (3, 3.5)]))
print(df_interval)
print(df_interval.index)

print("\nCreate an Interval Index using IntervalIndex.from_arrays:")
df_interval = pd.DataFrame({"X":[1, 2, 3, 4, 5, 6, 7]},             
                            index = pd.IntervalIndex.from_arrays(
                            [0, .5, 1, 1.5, 2, 2.5, 3], [.5, 1, 1.5, 2, 2.5, 3, 3.5]))
print(df_interval)
print(df_interval.index) 

