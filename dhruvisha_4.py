#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Name: Bhaliya Dhruvisha A.
# class: Sy bsc.it , sem = 4
# Enroll.no: SR22BSIT017
# Date: 30/01/2024
# div: B

# Assignment : 4
# Aim: Functions

# 1.Write a Python function to multiply all the numbers in a list1=[34,6,1,3]

def multiply_List(myList):
    result = 1
    for x in myList:
        result = result * x
    return result

list1 = [34, 6, 1, 3]
print(multiply_List(list1))


# In[6]:


# 2. Write a Python function to sum all the numbers in a list2=[3,5,6,7,8,1,0]

def sumlist(mylist):
 return sum(mylist)
    
list1 = [1,2,3,4,5,6]
print(sumlist(list1))


# In[7]:


# 3. Write a Python function that input number as a parameter and checks whether the
# number is prime or not.
# Note : A prime number (or a prime) is a natural number greater than 1 and that has no
# positive divisors other than 1 and itself.

def is_prime(number):
    if number > 1:
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return False
        return True
    return False
num = 7
print(f"{num} is prime: {is_prime(num)}")


# In[8]:


# 4. Write a Python function that checks whether a passed string is a palindrome or not.
# Note: A palindrome is a word, phrase, or sequence that reads the same backward as
# forward, e.g., madam or nurses run

def is_palindrome(s):
    return s == s[::-1]

# Example usage
string = "madam"
print(f"{string} is a palindrome: {is_palindrome(string)}")


# In[10]:


# 5. Write a Python program to reverse a string.
# Sample String : "Hello World"
# Expected Output : "dlroW olleH"

def reverse_string(s):
    return s[::-1]

# Example usage
input_string = "Hello World"
print(f"Original: {input_string}\nReversed: {reverse_string(input_string)}")


# In[11]:


# 6. Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]

def print_even_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    print(even_numbers)

# Example usage
sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print_even_numbers(sample_list)


# In[12]:


# 7.Write a Python function to calculate the factorial of a number.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Example usage
number = 5
print(f"The factorial of {number} is {factorial(number)}")


# In[13]:


# 8.Write a Python function that accepts a string and counts the number of upper and
# lower case letters.

# Sample String : ' Welcome To The World Of Python'
# Expected Output :
# No. of Uppercase characters : 6
# No. of Lower case Characters : 19

def count_upper_lower(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())
    print(f"No. of Uppercase characters: {upper_count}\nNo. of Lowercase characters: {lower_count}")

# Example usage
sample_string = 'Welcome To The World Of Python'
count_upper_lower(sample_string)


# In[14]:


# 9.Write a python function which counts vowels and constants in a word.

def count_vowels_consonants(word):
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in word if char in vowels)
    consonant_count = len(word) - vowel_count
    print(f"No. of Vowels: {vowel_count}\nNo. of Consonants: {consonant_count}")

# Example usage
input_word = "Python"
count_vowels_consonants(input_word)


# In[15]:


# 10. Write a python function that accepts radius and returns the area of a circle.

def area_of_circle(radius):
    return 3.14159 * radius**2

# Example usage
circle_radius = 5
print(f"The area of the circle with radius {circle_radius} is {area_of_circle(circle_radius)}")


# In[16]:


# 11.Write a python function that accepts lowercase words and returns uppercase words.

def convert_lowercase_to_uppercase(words):
    return [word.upper() for word in words]

# Example usage
lowercase_words = ["hello", "world", "python"]
print(f"Uppercase words: {convert_lowercase_to_uppercase(lowercase_words)}")


# In[17]:


# 12. Write a python function that accepts lowercase words and returns uppercase words.

def convert_lowercase_to_uppercase(words):
    return [word.upper() for word in words]

# Example usage
lowercase_words = ["hello", "world", "python"]
print(f"Uppercase words: {convert_lowercase_to_uppercase(lowercase_words)}")


# In[18]:


# 13. Write a Python function to find the maximum of three numbers.

def max_of_three(a, b, c):
    return max(a, b, c)

# Example usage
num_a, num_b, num_c = 12, 8, 15
print(f"The maximum of {num_a}, {num_b}, and {num_c} is {max_of_three(num_a, num_b, num_c)}")


# In[19]:


# 14. Write a python function for swap two inputted numbers.

def swap_numbers(a, b):
    return b, a

# Example usage
num1, num2 = 3, 7
num1, num2 = swap_numbers(num1, num2)
print(f"Swapped numbers: {num1}, {num2}")


# In[21]:


# 15. Write a python function which inputted 5 different numbers as list and sorted them.

def sort_numbers(numbers):
    return sorted(numbers)

# Example usage
input_numbers = [5, 2, 8, 1, 7]
sorted_numbers = sort_numbers(input_numbers)
print(f"Sorted numbers: {sorted_numbers}")

