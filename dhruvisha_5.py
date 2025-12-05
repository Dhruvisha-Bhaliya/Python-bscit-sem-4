#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Name: Bhaliya Dhruvisha A.
# class: Sy bsc.it , sem = 4
# Enroll.no: SR22BSIT017
# Date: 30/01/2024
# div: B

# Assignment-5

# Aim: text file handling in python

# 1. Write a Python program to read an entire text file.

file=open("/home/syitb/xyz.txt","r")

print("read function: ")
print(file.read())


# In[7]:


# 2. Write a Python program to read first n lines of a file

file=open("/home/syitb/xyz.txt","r")

print("readline function:")
print(file.readline())
print()


# In[12]:


# 3. Write a Python program to append text to a file and display the text.

file1 = open("/home/syitb/xyz.txt", "a")  # append mode
file1.write("python file handling\n")
file1.close()
 
file1 = open("/home/syitb/xyz.txt", "r")
print("Output of Readlines after appending")
print(file1.read())
print()
file1.close()
 


# In[22]:


# 4. Write a Python program to read last n lines of a file.
 
a_file = open("/home/syitb/xyz.txt", "r")
lines = a_file.readlines()

last_lines = lines[-n:]


print(last_lines)


# In[23]:


# 5. Write a Python program to read a file line by line and store it into a list.

file1 = '/home/syitb/xyz.txt' 

with open(file1, 'r') as file:
    lines = file.readlines()

# Displaying the lines
for line in lines:
    print(line.strip())

# Storing the lines in a list
lines_list = [line.strip() for line in lines]
print("\nLines stored in a list:")
print(lines_list)


# In[25]:


# 6. Write a Python program to read a file line by line store it into a variable.

def file_read(km):
        with open (km, "r") as myfile:
                data=myfile.readlines()
                print(data)
file_read('/home/syitb/xyz.txt')


# In[27]:


# 7. Write a Python program to read a file line by line store it into an list.

file1 = '/home/syitb/xyz.txt' 

with open(file1, 'r') as file:
    lines = file.readlines()

# Displaying the lines
for line in lines:
    print(line.strip())

# Storing the lines in a list
lines_list = [line.strip() for line in lines]
print("\nLines stored in a list:")
print(lines_list)


# In[28]:


# 8. Write a python program to find the longest words.

file1 = '/home/syitb/xyz.txt'

with open(file1, 'r') as file:
    words = file.read().split()

if not words:
    print("The file is empty.")
else:
    max_length = len(max(words, key=len))


    longest_words = [word for word in words if len(word) == max_length]
    print(f"The longest words in the file are: {longest_words}")


# In[29]:


# 9. Write a Python program to count the number of lines in a text file.

file1 = '/home/syitb/xyz.txt'

with open(file1, 'r') as fp:
	lines = len(fp.readlines())
	print('Total Number of lines:', lines)


# In[32]:


# 10. Write a Python program to count the frequency of words in a file.

from collections import Counter
def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())

print("Number of words in the file :",word_count("/home/syitb/xyz.txt"))


# In[33]:


# 11. Write a Python program to get the file size of a plain file.

def file_size(fname):
        import os
        statinfo = os.stat(fname)
        return statinfo.st_size

print("File size of a plain file: ",file_size("/home/syitb/xyz.txt"))


# In[55]:


# 12. Write a Python program to write a list to a file.


item = ['a', 'b', 'c', 'd'] 
file1 = open("/home/syitb/xyz.txt","w")
for li in item:
    file1.write(li+"\n")
file1.close()


# In[62]:


# 13. Write a Python program to copy the contents of a file to another file.

print("Enter the Name of Source File: ")
sFile = input()
print("Enter the Name of Target File: ")
tFile = input()

fileHandle = open(sFile, "r")
texts = fileHandle.readlines()
fileHandle.close()

fileHandle = open(tFile, "w")
for s in texts:
    fileHandle.write(s)
fileHandle.close()

print("\nFile Copied Successfully!")


# In[63]:


# 14. Write a Python program to combine each line from first file with the corresponding line in second file.

with open('/home/syitb/xyz.txt') as fh1, open('/home/syitb/chatgpt.txt') as fh2:
    for line1, line2 in zip(fh1, fh2):
        # line1 from abc.txt, line2 from test.txtg
        print(line1+line2)
		


# In[66]:


# 15. Write a Python program that takes a text file as input and returns the number
# of words of a given text file. Take any file for example.
# Note: Some words can be separated by a comma with no space.

def count_words(filepath):
 with open(filepath) as f:
       data = f.read()
       data.replace(",", " ")
       return len(data.split(" "))
print(count_words("/home/syitb/xyz.txt"))


# In[3]:


# 16. Write a function that counts and display the number of 5 letter words in a text file “Sample.txt”

text = open("/home/syitb/chatgpt.txt", "r") 
d = dict() 

for line in text: 
	line = line.strip() 
	line = line.lower() 
	words = line.split(" ") 
					
	for word in words:  
		if word in d: 
			d[word] = d[word] + 1
		else: 
			d[word] = 1

for key in list(d.keys()): 
	print(key, ":", d[key]) 


# In[4]:


# 17. Write a function VowelCount() in Python, which should read each character of a text
# file MY_TEXT_FILE.TXT, should count and display the occurrence of alphabets
# vowels.

def VowelCount(file_path):
    vowels = 'aeiouAEIOU'
    file = open(file_path, 'r')
    characters = file.read()
    vowel_count = sum(1 for char in characters if char in vowels)
    print("Vowel count:", vowel_count)
    file.close()


# Call the VowelCount() function with the desired file path
VowelCount("/home/syitb/chatgpt.txt")

