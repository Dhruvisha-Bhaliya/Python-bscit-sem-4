# 4. Set & Dictionary:--------------

info = {
   "name": "dhruvi",
    "subjects": ["python", "C", "Java"],
    "Topics": ("dict", "set"),
    "learn": "coding",
    "age": 24,
    "is_adult": True,
    "marks": 94.4
}

info["name"] = "dhruvibhaliya"
print(info)
print(info["subjects"])
print(info["Topics"])

# Nested Dictionaries:-----------------

student = {
    "name": "dhruvipatel",
    "score": {
    "chem": 98,
     "phy": 67,
        "math": 56
     }
}
print(student["score"]["math"])

# Dictionary Methods:-----------

print(info.keys()) # returns all keys

print(info.values()) # returns all values

print(info.items()) # returns all(key,val) pairs as tuples

print(info.get("name")) # returns the key accroding to value

print(info.update({"name":"khushi"})) # inserts the specified items to the dictionary

print(info["name"])

nums = {1, 2, 3, 4, 2}
nums2 = {2, 3, 4, 5, 6}

print(nums.add(6)) # adds an element
print(nums)

print(nums.remove(2)) # removes the element
print(nums)

# print(nums.clear()) # empties the set
print(nums)

print(nums.pop()) # removes a random value
print(nums)

print(nums.union(nums2)) # combines both set values & returns new

print(nums.intersection(nums2)) # combines common values & returns new


# WAP Store following word meanings in a python dictionary:

dict = {
    "cat": "a small animal",
    "table": ["a piece of furniture", "list of facts & figures"]
}

print(dict)

# You are given a list of subjects for students.Assume one classroom is required for 1 subject.How many classrooms are
# needed by all students.

subjects = {
    "python", "java", "c++", "python", "javascript", "java",
    "python", "java", "c++", "C"
}

print(len(subjects))

# WAP to enter marks of 3 subjects from the user and store them in a dictionary.Start with an empty dictionary
# & add one by one. Use subject name as key & marks as value.

marks = {}

x = int(input("Enter Account: "))
marks.update({"Account" : x})

x = int(input("Enter Statistics: "))
marks.update({"Statistics" : x})

x = int(input("Enter Economics: "))
marks.update({"Economics" : x})

print(marks)

# Figure out a way to store 9 & 9.0 as separate values in the set.
# (You can take help of built-in data types)

values = {
    ("float", 9.0),
    ("int", 9)
}
print(values)


