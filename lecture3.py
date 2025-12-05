# 3. Lists & Tuples:----------------------------

marks = [94.4, 87.5, 95.2, 66.4, 51.2]
print(marks)

print(type(marks))

print(len(marks))
print(marks[0])

student = ["karan", 95.4, 19, "Surat"]
print(student)
student[0] = "Arjun"
print(student)

# List Slicing:---------

marks = [87, 95, 45, 67, 12]
print(marks[1:])
print(marks[:1])
print(marks[-3:-1])

# List Methods:-----------------------------

print(marks.append(97))
print(marks)

print(marks.sort())
print(marks)

print(marks.sort(reverse=True))
print(marks)

print(marks.reverse())
print(marks)

print(marks.insert(3,78))
print(marks)

list1 = [2, 1, 3, 1]

print(list1.remove(1))
print(list1)

list1.pop(2)
print(list1)

#Tuples:---------------

tup = (2, 1, 3, 1, 1)
print(tup[0])
print(tup[1])

tup2 = ()
print(tup2)
print(type(tup2))

print(tup.index(1))
print(tup.count(1))

# WAP to ask the user to enter names of their 3 favorite movies & store them in a list

movies = []
movies.append(input("Enter 1st movie: "))
movies.append(input("Enter 2st movie: "))
movies.append(input("Enter 3st movie: "))
print(movies)

# WAP to check if a list contains a palindrome of elements.(Hint:use copy() method)

lis = [1, 2, 1]
lis2 = [1, 2, 3]
copylis = lis.copy()
copylis.reverse()

if(copylis == lis):
    print("palindrome")
else:
    print("not palindrome")

# WAP to count the number of students with the "A" grade in the following tuple.

grades = ("C","D","A","A","B","B","A")
print(grades.count("A"))

# WAP the above values in a list & sort them from "A" to "D".

grade = ["C","D","A","A","B","B","A"]

grade.sort()
print(grade)