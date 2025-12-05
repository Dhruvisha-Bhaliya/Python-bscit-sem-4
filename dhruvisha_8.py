#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Assignment-8

# Aim: Matplotlib library exercise

# 1. EXAMPLE :
    
from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')
x = [5,8,10]
y = [12,16,6]
x2 = [6,9,11]
y2 = [6,15,7]
plt.plot(x,y,'g',label='line one', linewidth=5)
plt.plot(x2,y2,'c',label='line two',linewidth=5)
plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.legend()
plt.grid(True,color='k')
plt.show()


# In[2]:


# 2. Example :
    
from matplotlib import pyplot as plt
plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],
label="BMW",width=.5)
plt.bar([.75,1.75,2.75,3.75,4.75],[80,20,20,50,60],
label="Audi", color='r',width=.5)
plt.legend()
plt.xlabel('Days')
plt.ylabel('Distance (kms)')
plt.title('Information')
plt.show()


# In[4]:


# 3. Example:

import matplotlib.pyplot as plt
population_age =[22,55,62,45,21,22,34,42,42,4,2,102,95,85,55,110,120,70,65,55,111,115,80,75,65,54,44,43,42,48]
bins = [0,10,20,30,40,50,60,70,80,90,100]
plt.hist(population_age, bins, histtype='bar', rwidth=0.8)
plt.xlabel('age groups')
plt.ylabel('Number of people')
plt.title('Histogram')
plt.show()


# In[5]:


# 4. Example:

import matplotlib.pyplot as plt
x = [1,1.5,2,2.5,3,3.5,3.6]
y = [7.5,8,8.5,9,9.5,10,10.5]
x1=[8,8.5,9,9.5,10,10.5,11]
y1=[3,3.5,3.7,4,4.5,5,5.2]
plt.scatter(x,y, label='high income low saving',color='r')
plt.scatter(x1,y1,label='low income high savings',color='b')
plt.xlabel('saving*100')
plt.ylabel('income*1000')
plt.title('Scatter Plot')
plt.legend()
plt.show()


# In[6]:


# 5. Example:
    
import matplotlib.pyplot as plt
days = [1,2,3,4,5]
sleeping =[7,8,6,11,7]
eating = [2,3,4,3,2]
working =[7,8,7,2,2]
playing = [8,5,7,8,13]
slices = [7,2,2,13]
activities = ['sleeping','eating','working','playing']
cols = ['c','m','r','b']
plt.pie(slices,
labels=activities,
colors=cols,
startangle=90,
shadow= True,
explode=(0,0.1,0,0),
autopct='%1.1f%%')
plt.title('Pie Plot')
plt.show()


# In[9]:


# 6. Example of dataframe

# importing package
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# create data
df = pd.DataFrame([['A', 10, 20, 10, 26], ['B', 20, 25, 15, 21], ['C', 12,15, 19, 6],['D', 10, 18, 11, 19]], 
columns=['Team', 'Round 1', 'Round 2','Round 3', 'Round 4'])
# view data
print(df)
# plot data in stack manner of bar type
df.plot(x='Team', kind='bar', stacked=True,title='Stacked Bar Graph by dataframe')
plt.show()


# In[14]:


"""
Self exercise:

1. Draw a line in a diagram from position (0,0) to position (6,250)
"""

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0,0])
ypoints = np.array([6,250])

plt.plot(xpoints,ypoints)
plt.show()


# In[16]:


"""
2. Draw a line in a diagram from position (1, 3) to position (8, 10) with
different line style.
[Hint: Use a dashed line:
plt.plot(ypoints, linestyle = 'dashed') ]
"""

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1,3])
ypoints = np.array([8,10])

plt.plot(ypoints, linestyle = 'dashed') 
plt.show()


# In[17]:


"""
3. Draw two points in the diagram, one at position (1, 3) and one in
position (8, 10)
"""


import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1,3])
ypoints = np.array([8,10])

plt.plot(xpoints, ypoints,'o') 
plt.show()


# In[19]:


"""
4. Draw a line in a diagram from position (1, 3) to (2, 8) then to (6, 1)
and finally to position (8, 10)Use different symbol for points.
"""


import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1,2,6,8])
ypoints = np.array([3,8,1,10])

plt.plot(xpoints,ypoints,marker='o') 
plt.show()

