# 8.Write a python program to check if a number entered by the user is a two digit,
# three digit or a four digit number.

number = int(input("Enter number: "))

if(number >= 0 and number <= 9) :
    print("single digit")
elif (number >= 10 and number <= 99) :
    print("two digit")
elif (number >= 100 and number <= 999):
    print("three digit")
elif (number >= 1000 and number <= 9999):
    print("four digit")
else :
    print("no output")
