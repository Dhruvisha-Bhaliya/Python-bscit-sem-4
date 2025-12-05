#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Name: Bhaliya Dhruvisha A.
# class: Sy bsc.it , sem = 4
# Enroll.no: SR22BSIT017
# Date: 06/02/2024
# div: B

# Assignment-6

# Aim: Numpy library - array handling

# 1. Example:

# Python Program to create array with all zeros

import numpy as np
a = np.zeros(3, dtype = int)
print("Matrix a : \n", a)
b = np.zeros([3, 3], dtype = int)
print("\nMatrix b : \n", b)


# In[2]:


# 2. Example:

import numpy as np
a = np.array([[1,2,3],
[4,5,6]])
b = np.array([[10,11,12],
[13,14,15]])
c = a + b
print(c)


# In[3]:


# 3. Example-3

a = np.array([[1,2,3],
[4,5,6]])
b = 2*a # multiplying the numpy array a(matrix) by 2
print(b)


# In[4]:


# Example 4: Identity Matrix

i = np.eye(4)
print(i)


# In[5]:


# Example 5: Array re-dimensioning

a = np.array([x for x in range(27)])
o = a.reshape((3,3,3))
print(o)


# In[6]:


# Example 6: Array datatype conversion

a = np.array([[2.5, 3.8, 1.5],
[4.7, 2.9, 1.56]])
o = a.astype('int')
print(o)


# In[7]:


# example 7: Boolean array:

a = np.array([[1, 0, 0],
[1, 1, 1],
[0, 0, 0]])
o = a.astype('bool')
print(o)


# In[8]:


# EXERCISE 8 - Horizontal Stacking of Numpy Arrays

# Stack 2 numpy arrays horizontally i.e., 2 arrays having the same 1st dimension (number of rows in 2D arrays)

a1 = np.array([[1,2,3],
[4,5,6]])
a2 = np.array([[7,8,9],
[10,11,12]])
o = np.hstack((a1, a2))
print(o)


# In[9]:


# EXERCISE 9 - Vertically Stacking of Numpy Arrays

# Stack 2 numpy arrays vertically i.e., 2 arrays having the same last dimension (number of columns in 2D arrays)

# Sample Solution

a1 = np.array([[1,2],
[3,4],
[5,6]])
a2 = np.array([[7,8],
[9,10],
[10,11]])
o = np.vstack((a1, a2))
print(o)


# In[18]:


# EXERCISE 9 - Custom Sequence Generation

# Generate a sequence of numbers in the form of a numpy array from 0 to 100 with gaps 
# of 2 numbers, for example: 0, 2, 4 

# Sample Solution

list_of_numbers = [x for x in range(0, 101, 2)]
o = np.array(list_of_numbers)
print(o)


# In[17]:


# Alternative 

o = np.arange(0, 101, 2)
print(o)


# In[12]:


# EXERCISE 10 - Getting the positions (indexes) where elements of 2 numpy

# arrays match
# From 2 numpy arrays, extract the indexes in which the elements in the 2 arrays match
# Sample Solution

a = np.array([1,2,3,4,5])
b = np.array([1,3,2,4,5])
print(np.where(a == b))


# In[13]:


# EXERCISE 11 - Generation of given count of equally spaced numbers within a specified range

# Output a sequence of equally gapped 5 numbers in the range 0 to 100 (both inclusive)

# Sample Solution

o = np.linspace(0, 100, 5)
print(o)


# In[19]:


# EXERCISE 12 - Matrix Generation with one particular value

# Output a matrix (numpy array) of dimension 2-by-3 with each and every value equal to 5

# Sample Solution

o = np.full((2, 3), 5)
print(o)


# In[20]:


# Alternate Solution

a = np.ones((2, 3))
o = 5*a
print(o)


# In[15]:


# EXERCISE 13 - Array Generation by repeatition of a small array across each dimension

# Output an array by repeating a smaller array of 2 dimensions, 10 times

# Sample Solution

a = np.array([[1,2,3],
[4,5,6]])
o = np.tile(a, 10)
print(o)


# In[16]:


# example 14: slicing

arr = np.arange(9).reshape(3,3)
print('Original array')
arr
print("\nModified array")
arr[:, ::-1]


# In[21]:


# 1. Write a NumPy program to convert a list of numeric values into a one-dimensional NumPy array.

# Expected Output:

# Original List: [12.23, 13.32, 100, 36.32]
# One-dimensional NumPy array: [ 12.23 13.32 100. 36.32]


import numpy as np
l = [12.23, 13.32, 100, 36.32]
print("Original List:", l)
a = np.array(l)
print("One-dimensional NumPy array: ", a)


# In[22]:


# 2. Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.

# Expected Output:

# [[ 2 3 4]
# [ 5 6 7]
# [ 8 9 10]]

import numpy as np
x = np.arange(2, 11).reshape(3, 3)
print(x)


# In[23]:


# 3. Write a NumPy program to create a null vector of size 10 and update the sixth value to 11.

# [ 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
# Update sixth value to 11
# [ 0. 0. 0. 0. 0. 0. 11. 0. 0. 0.]

import numpy as np
x = np.zeros(10)
print(x)
print("Update sixth value to 11")
x[6] = 11
print(x)


# In[24]:


# 4. Write a NumPy program to create an array with values ranging from 12 to 38.

# Expected Output:

# [12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]

import numpy as np
x = np.arange(12,38)
print(x)


# In[27]:


# 5. Write a NumPy program to reverse an array (the first element becomes the last).

# Original array:
# [12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]

# Reverse array:
# [37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12]

import numpy as np
x = np.arange(12,38)
print(x)

a = x[::-1]
print(a)


# In[28]:


# 6. Write a NumPy program to convert an array to a floating type.

# Sample output:

#Original array
# [1, 2, 3, 4]

# Array converted to a float type:
# [ 1. 2. 3. 4.]

import numpy as np
a = [1, 2, 3, 4]
print("Original array")
print(a)
x = np.asfarray(a)
print("Array converted to a float type:")
print(x)


# In[36]:


# 7. Write a NumPy program to create an 8x8 matrix and fill it with a checkerboard pattern.

# Checkerboard pattern:
# [[0 1 0 1 0 1 0 1]

# [0 1 0 1 0 1 0 1]
# [1 0 1 0 1 0 1 0]]

import numpy as np
x = np.ones((3, 3))
print("Checkerboard pattern:")
x = np.zeros((2,8), dtype=int)
x[1::2, ::2] = 1  
x[::2, 1::2] = 1 
print(x) 


# In[37]:


# 8. Write a NumPy program to convert a list and tuple into arrays.

# List to array:
# [1 2 3 4 5 6 7 8]

# Tuple to array:
# [[8 4 6]
# [1 2 3]]

import numpy as np
list = [1, 2, 3, 4, 5, 6, 7, 8]
print("List to array: ")
print(np.asarray(list))
tuple = ([8, 4, 6], [1, 2, 3])
print("Tuple to array: ")
print(np.asarray(tuple))


# In[42]:


# 9. Write a NumPy program to append values to the end of an array.

# Expected Output:

# Original array:
# [10, 20, 30]
# After append values to the end of the array:
# [10 20 30 40 50 60 70 80 90]

import numpy as np
l = [10,20,30]
print("Orijinal array: ")
print(l)
print("After append values to the end of the array: ")
x = np.append(x, [[40, 50, 60], [70, 80, 90]])
print(x)


# In[43]:


# 10. Write a NumPy program to test whether each element of a 1-D array is also present in a second array.

# Expected Output:

# Array1: [ 0 10 20 40 60]
# Array2: [0, 40]

# Compare each element of array1 and array2
# [ True False False True False]

import numpy as np
array1 = np.array([0, 10, 20, 40, 60])
print("Array1: ", array1)
array2 = [0, 40]
print("Array2: ", array2)
print("Compare each element of array1 and array2")
print(np.in1d(array1, array2))


# In[45]:


# 11. Python program to add two Matrices

# Program to add two matrices using nested loop

X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[2,3,4],
    [5,6,7],
    [8,9,2]]


result = [[0,0,0],
        [0,0,0],
        [0,0,0]]

for i in range(len(X)): 
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]

for r in result:
    print(r)


# In[46]:


# 12. Python program to multiply two matrices

X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[2,3,4],
    [5,6,7],
    [8,9,2]]

result = [[0,0,0],
        [0,0,0],
        [0,0,0]]

for i in range(len(X)): 
    for j in range(len(X[0])):
        result[i][j] = X[i][j] * Y[i][j]

for r in result:
    print(r)


# In[2]:


# 13. Python program for Matrix Product

def Multi(A,B):
    result=[ [0,0,0],[0,0,0],[0,0,0] ]
    #for rows
    for i in range(len(A)):
        #for columns
        for j in range(len(B[0])):
            #for rows of matrix B
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    for p in result:
        print(p)
    return 0

A = [ [1, 2, 3],[6, 7, 4], [8, 10, 11] ]
B = [[1, 5, 3],[2, 6, 5], [7, 4, 9] ]

print("Result: ")
Multi(A,B)


# In[47]:


# 14. Adding and Subtracting Matrices in Python

import numpy as np
A = np.array([[1, 2], [3, 4]])
B = np.array([[4, 5], [6, 7]])
print("Printing elements of first matrix")
print(A)
print("Printing elements of second matrix")
print(B)
print("Addition of two matrix")
print(np.add(A, B))


# In[51]:


# 15. Transpose a matrix in Single line in Python

mat= [ [1,2],[3,4],[5,6]]

for m in mat:
    print(m)

trans= [ [mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
print("Trans: ")

for t in trans:
    print(t)


# In[1]:


# 16. Python | Matrix creation of n*n

n = 4
matrix = [list(range(1 + n * i, 1 + n * (i + 1))) for i in range(n)]
print("The created matrix of {} * {}: ".format(n,n))
for m in matrix:
    print(m)


# In[2]:


# Advanced:

# 1. Write a NumPy program to find the indices of the maximum and minimum values along the given axis of an array.

# Original array: [1 2 3 4 5 6]
# Maximum Values: 5
# Minimum Values: 0

import numpy as np
x = np.array([1, 2, 3, 4, 5, 6])
print("Original array: ", x)
print("Maximum Values: ", np.argmax(x))
print("Minimum Values: ", np.argmin(x))


# In[3]:


# 2. Write a NumPy program to change an array's dimension.

# Expected Output:
# 6 rows and 0 columns
# (6,)
# (3, 3) -> 3 rows and 3 columns
# [[1 2 3]
# [4 5 6]
# [7 8 9]]
# Change array shape to (3, 3) -> 3 rows and 3 columns
# [[1 2 3]
# [4 5 6]
# [7 8 9]]

import numpy as np
x = np.array([1, 2, 3, 4, 5, 6])
print("6 rows and 0 columns")
print(x.shape)
y = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("(3, 3) -> 3 rows and 3 columns ")
print(y)
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
x.shape = (3, 3)
print("Change array shape to (3, 3) -> 3 rows and 3 columns ")
print(x) 


# In[4]:


# 3. Write a NumPy program to create another shape from an array without changing its data.
# Reshape 3x2:
# [[1 2]
# [3 4]
# [5 6]]
# Reshape 2x3:
# [[1 2 3]
# [4 5 6]]

import numpy as np
x = np.array([1, 2, 3, 4, 5, 6])
y = np.reshape(x, (3, 2))
print("Reshape 3x2:")  
print(y)  
z = np.reshape(x, (2, 3))
print("Reshape 2x3:")  
print(z)  


# In[1]:


"""
4. Write a NumPy program to create a new array of 3*5, filled with 2.
Expected Output:
[[2 2 2 2 2]
[2 2 2 2 2]
[2 2 2 2 2]]
[[2 2 2 2 2]
[2 2 2 2 2]
[2 2 2 2 2]
"""

import numpy as np
x = np.full((3, 5), 2, dtype=np.uint)
print(x)
y = np.ones([3, 5], dtype=np.uint) * 2
print(y) 


# In[2]:


"""
5. Write a NumPy program to find the 4th element of a specified array.
Expected Output:
[[ 2 4 6]
[ 6 8 10]]
Forth e1ement of the array:
6
"""

import numpy as np
x = np.array([[2, 4, 6], [6, 8, 10]], np.int32)
print(x)
e1 = x.flat[3]
print("Fourth element of the array:")
print(e1) 

