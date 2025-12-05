#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Name: Bhaliya Dhruvisha A.
# class: Sy bsc.it , sem = 4
# Enroll.no: SR22BSIT017
# Date: 27/02/2024
# div: B

# Assignment 10

# Aim:Pandas Library using CSV file

# 1. Write a python code to show the first 5 rows of the dataframe. (Hint:Use a Head() function)

import pandas as pd
file=open("/home/syitb/B_dhruvisha/weather.csv","r");
df = pd.DataFrame(file)
print(df.head())


# In[5]:


# 2. Write a python code to show a last 5 rows of the dataframe (Hint : Use a Tail() function )

import pandas as pd
file=open("/home/syitb/B_dhruvisha/weather.csv","r");
df = pd.DataFrame(file)
print(df.tail())


# In[6]:


# 3.Write a python code to shows the total no. of rows and no. of column of the data frame(Hint: Use a shape method)

import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('/home/syitb/B_dhruvisha/weather.csv')

# Display the total number of rows and columns
num_rows, num_columns = df.shape
print(f'Total number of rows: {num_rows}')
print(f'Total number of columns: {num_columns}')


# In[7]:


# 4.write a python code to find the index of the dataframe. (Hint: Use a Index method)

import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('/home/syitb/B_dhruvisha/weather.csv')

# Get the index of the DataFrame
index_values = df.index

print(f'Index of the DataFrame: {index_values}')


# In[8]:


# 5. write a python code to display only the column name. (Hint: Use Column method)

import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('/home/syitb/B_dhruvisha/weather.csv')

# Get the column names of the DataFrame
column_names = df.columns
print(f'Column names of the DataFrame: {column_names}')


# In[9]:


# 6. write a python code to show the data-type of each column. (Hint: Use dtype method)

import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('/home/syitb/B_dhruvisha/weather.csv')

# Get the data types of each column in the DataFrame
column_data_types = df.dtypes

print('Data types of each column in the DataFrame:')
print(column_data_types)


# In[10]:


# 7. Write a python code to show basic information about the dataframe. (Hint: Use a info() function)

import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('/home/syitb/B_dhruvisha/weather.csv')

# Display basic information about the DataFrame
df.info()


# In[11]:


# 8. Write a python code to show a total no. of values in each column. (Hint: Use a count() function)

import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('/home/syitb/B_dhruvisha/weather.csv')

# Display the total number of values in each column
column_value_counts = df.count()
print('Total number of values in each column:')
print(column_value_counts)


# In[12]:


# 9. Write a python code to show all the unique values of each column. (Hint: Use dataframe[‘column_name’].unique())

import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('/home/syitb/B_dhruvisha/weather.csv')

# Display all the unique values of each column
for column in df.columns:
    unique_values = df[column].unique()
    print(f'Unique values in column "{column}":')
    print(unique_values)


# In[14]:


# 10. Find all the unique “wind speed” values in the data. (Hint : Use dataframe['Column_Name'].nunique())

import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('/home/syitb/B_dhruvisha/weather.csv')

# Find the number of unique 'wind speed' values
unique_wind_speed_values = df['Wind Speed_km/h'].nunique()

print("Number of unique wind speed values:", unique_wind_speed_values)


# In[17]:


# 11. Find the number of times when the weather is exactly clear. (Hint: Use dataframe.groupby(‘Column_name’).
# get_group('column_ name'))

import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('/home/syitb/B_dhruvisha/weather.csv')

# Group the DataFrame by the 'weather' column and get the group where weather is 'clear'
clear_weather_group = df.groupby('Weather').get_group('Clear')

# Get the count of rows where weather is 'clear'
clear_weather_count = clear_weather_group.shape[0]

print("The number of times when the weather is exactly clear is:", clear_weather_count)


# In[19]:


# 12. Find a number of times when the “wind speed” was exactly 4 km/h. (Hint: dataframe[dataframe['Column_name'] 
# == 4])

import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('/home/syitb/B_dhruvisha/weather.csv')

# Filter the DataFrame for rows where the "wind speed" column is equal to 4
result = df[df['Wind Speed_km/h'] == 4]

# Get the number of times the "wind speed" was exactly 4 km/h
count = len(result)

print(count)


# In[20]:


# 13. Find out all the null values in the data. (Hint: Use dataframe.isnull().sum())

import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('/home/syitb/B_dhruvisha/weather.csv')

# Find out all the null values in the data
null_values = df.isnull().sum()

print(null_values)


# In[24]:


# 14. Find all the instances of when “wind speed is above 24” and “visibility is 25” 
# (Hint:dataframe[(dataframe['column_name'] > 24) & (df['column_name'] == 25)])

import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('/home/syitb/B_dhruvisha/weather.csv')

# Find out all the null values in the data
speed = df[(df['Wind Speed_km/h'] > 24) & (df['Visibility_km'] == 25)]

count = len(speed)

print(count)


# In[30]:


# 15. find the mean value of each column against each “weather condition”. (Hint:
# dataframe.groupby(‘column_name').mean())

import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('/home/syitb/B_dhruvisha/weather.csv')

mean_value =[( df.groupby('Weather').mean())]

print(mean_value)


# In[32]:


# 16. Find the min and max value of each column against each “weather condition”(Hint:
# df.groupby('Weather').max())

import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('/home/syitb/B_dhruvisha/weather.csv')

max_value =[( df.groupby('Weather').max())]

print(max_value)

