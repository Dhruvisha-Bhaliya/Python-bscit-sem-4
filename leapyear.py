# 3.Write a python program to check if a year is a leap year or not.

year = int(input("Enter a year: "))

if year % 4 == 0 :
    print(year," is leap year")
else :
    print(year," is not leap year")
