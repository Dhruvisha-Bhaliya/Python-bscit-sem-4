#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Name: Bhaliya Dhruvisha A.
# class: Sy bsc.it , sem = 4
# Enroll.no: SR22BSIT017
# Date: 13/02/2024
# div: B

# Assignment 9

"""
1. Find mean, median, mode and standard deviation values from a tuple of
20 decimal values of stock market prices.
"""

n_num = (12.4,56.8,45.8,23.6,12.9,98.7,56.2,34.7,45.8,23.6,78.9,45.7,23.7,21.8,65.6,34.8,89.7,56.3,56.9,23.0)
n = len(n_num) 

get_sum = sum(n_num) 
mean = get_sum / n 

print("Mean / Average is: " + str(mean)) 


n_num = (12.4,56.8,45.8,23.6,12.9,98.7,56.2,34.7,45.8,23.6,78.9,45.7,23.7,21.8,65.6,34.8,89.7,56.3,56.9,23.0)
n = len(n_num) 

if n % 2 == 0: 
	median1 = n_num[n//2] 
	median2 = n_num[n//2 - 1] 
	median = (median1 + median2)/2
else: 
	median = n_num[n//2] 
print("Median is: " + str(median)) 

# Python program to print 
# mode of elements 
from collections import Counter 


n_num = (12.4,56.8,45.8,23.9,12.9,98.7,56.2,34.7,45.8,23.6,78.9,45.7,23.7,21.8,65.6,34.8,89.7,56.3,56.9,23.0)
n = len(n_num) 

data = Counter(n_num) 
get_mode = dict(data) 
mode = [k for k, v in get_mode.items() if v == max(list(data.values()))] 

if len(mode) == n: 
	get_mode = "No mode found"
else: 
	get_mode = "Mode is / are: " + ', '.join(map(str, mode)) 
	
print(get_mode) 


test_list = (12.4,56.8,45.8,23.9,12.9,98.7,56.2,34.7,45.8,23.6,78.9,45.7,23.7,21.8,65.6,34.8,89.7,56.3,56.9,23.0)

print("The original list : " + str(test_list)) 


mean = sum(test_list) / len(test_list) 
variance = sum([((x - mean) ** 2) for x in test_list]) / len(test_list) 
res = variance ** 0.5


print("Standard deviation of sample is : " + str(res)) 


# In[11]:


# 2. Create a python function to create cosine values of a given square matrix.

import numpy as np
import math

in_array = [0, math.pi / 2, np.pi / 3, np.pi]
print ("Input array : \n", in_array)

cos_Values = np.cos(in_array)
print ("\nCosine values : \n", cos_Values)


# In[4]:


# 3. Create a dictionary of words and their synonyms. Search word and its
# synonym from dictionary. Add new words to dictionary with its meaning.

word_dict = {}
def search_word(word):
    if word in word_dict:
        return word_dict[word]
    else:
        return "Word not found in the dictionary."

def add_word(word, synonyms):
    word_dict[word] = synonyms

add_word("happy", ["joyful", "content", "pleased"])
add_word("sad", ["unhappy", "mournful", "depressed"])

search_word("sad")


# In[6]:


# 4. Take input of text file and find word count for each unique word.

# Read the text file
with open('/home/syitb/chatgpt.txt', 'r') as file:
    content = file.read()

# Split the content into words
words = content.split()

# Create a dictionary to store word counts
word_counts = {}

# Iterate through the words and update counts
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

# Print out the word counts for each unique word
for word, count in word_counts.items():
    print(f'{word}: {count}')


# In[10]:


# 5. Take input of word file and remove given stop-words from the content as given in the list in python.

# Define the list of stop words
stop_words = ['the', 'and', 'is', 'in', 'on', 'it']

# Open the word file for reading
with open('/home/syitb/chatgpt.txt', 'r') as file:
    # Read the content of the file
    content = file.read()
    
    # Split the content into words
    words = content.split()
    
    # Remove stop words from the content
    filtered_words = [word for word in words if word.lower() not in stop_words]
    
    # Join the filtered words back into a string
    updated_content = ' '.join(filtered_words)

# Print the updated content without stop words
print(updated_content)


# In[18]:


# 6. Create a random numpy array of and find out its shape and dimenation using numpy functions.

import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape) 


# In[19]:


# 7. Write a Python script to print a dictionary where the keys are numbers between 1 and15 (both included) 
# and the values are square of keys.

# Create an empty dictionary 'd' to store the squares of numbers.
d = dict()

# Iterate through numbers from 1 to 15 (inclusive).
for x in range(1, 16):
    # Calculate the square of each number and store it in the dictionary 'd' with the number as the key.
    d[x] = x ** 2

# Print the dictionary 'd' containing the squares of numbers from 1 to 15.
print(d)


# In[22]:


# 8. Write a Python program to combine two dictionary adding values for common keys.
# Write a Python program to find the highest 3 values in a dictionary

# Import the 'Counter' class from the 'collections' module.
from collections import Counter

# Create two dictionaries 'd1' and 'd2' with key-value pairs.
d1 = {'a': 400, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 300, 'd': 400}

# Use the 'Counter' class to create counter objects for 'd1' and 'd2', which count the occurrences of each key.
# Then, add the counters together to merge the key-value pairs and their counts.
d = Counter(d1) + Counter(d2)

# Print the resulting merged dictionary 'd'.
print(d)

from collections import Counter
 
# Initial Dictionary
my_dict = d

k = Counter(my_dict)
 
# Finding 3 highest values
high = k.most_common(3) 
 
print("Initial Dictionary:")
print(my_dict, "\n")
 
 
print("Dictionary with 3 highest values:")
print("Keys: Values")
 
for i in high:
    print(i[0]," :",i[1]," ")


# In[23]:


"""9. Write a Python program to create and display all combinations of letters, selecting each letter from 
 a different key in a dictionary.

Sample data : {'1':['a','b'],
'2':['c','d']}
Output:
Ac
Ad
Bc
Bd """

# Import the 'itertools' module, which provides tools for working with iterators and iterable objects.
import itertools

# Create a dictionary 'd' with keys '1' and '2', and associated lists of characters as values.
d = {'1': ['a', 'b'], '2': ['c', 'd']}

# Iterate through combinations of values from the dictionary 'd' using 'itertools.product'.
# The values are sorted based on their keys to ensure a specific order.
for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
    # Print the combinations as strings by joining the characters in each combination.
    print(''.join(combo))


# In[28]:


# Create a dictionary for state, capitals and rank for living. Sort data to find top 5 higher ranking states to live.

# Create a dictionary for states, capitals, and their ranking for living
state_data = {
    'California': {'capital': 'Sacramento', 'rank': 1},
    'Texas': {'capital': 'Austin', 'rank': 2},
    'New York': {'capital': 'Albany', 'rank': 3},
    'Florida': {'capital': 'Tallahassee', 'rank': 4},
    'Illinois': {'capital': 'Springfield', 'rank': 5},
    'Colorado': {'capital': 'Denver', 'rank': 6},
    'Washington': {'capital': 'Olympia', 'rank': 7},
    'Massachusetts': {'capital': 'Boston', 'rank': 8},
    'Virginia': {'capital': 'Richmond', 'rank': 9},
    'Oregon': {'capital': 'Salem', 'rank': 10}
}

# Sort the state data based on the ranking
sorted_states = sorted(state_data.items(), key=lambda x: x[1]['rank'])

# Find the top 5 highest-ranking states to live
top_5_states = sorted_states[:5]

# Print the top 5 highest-ranking states to live
for state, data in top_5_states:
    print(f"{state}: Capital - {data['capital']}, Rank - {data['rank']}")


# In[ ]:




