# 7.Write a python program to take input of marks in two subjects. Calculate percentage and based on percentage
# , display grades as below:
# >=70 : Distinction
# Between 60-69: first class
# Between 50-59 : second class
# Between 40-49 : Pass class
# Less than 40 : fail

marks = int(input("Enter marks: "))

if marks >= 70 :
    print("Distinction")
elif (marks >= 60 and marks <= 69) :
    print("first class")
elif (marks >= 50 and marks <= 59) :
    print("second class")
elif (marks >= 40 and marks <= 49) :
    print("Pass class")
elif marks < 40  :
    print("fail")
