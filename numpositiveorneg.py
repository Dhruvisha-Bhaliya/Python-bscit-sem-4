# 5. Write a python program to check if a number is zero, positive or negative.

num = int(input("Enter number: "))

if num > 0  :
    print(num , " is positive")
elif num < 0 :
    print(num , " is negative")
else :
    print(num , " is zero")