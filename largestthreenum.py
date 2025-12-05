# 4.Write a python program to find largest of 3 numbers.
# a.	Do it using logical operators
# Do it using nested if


a = int(input("Enter number1: "))
b = int(input("Enter number2: "))
c = int(input("Enter number3: "))

if a > b and a > c :
    print("a is larger than b and c")
elif b > c and b > a:
    print("b is larger than a and c")
else :
    print("c is larger than  a and b")
