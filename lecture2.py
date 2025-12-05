# ---------------------------2.STRINGS & CONDITIONAL STATEMENTS--------------------------

str1 = "This is a string."
str2 = "This is an apple."
str3 = """this is a string."""

# functions:---------------------

str = "I am studying python from ApneaCollege."

print(str.endswith("ege"))

print(str.capitalize())

print(str.replace("python", "java"))

print(str.find("python"))

print(str.count("o"))

# WAP to input user's first name & print its length.

name = input("Enter user name: ")
print(len(name))

# WAP to find the occurrence of '$' in String.

str4 = "HI, $iam the $ symbol $99.99."
print(str4.count("$"))

# Conditional Statements:----------------------------------

age = 1

if age >= 18:
    print("can vote & apply for license")
else:
    print("can not vote & not apply for license")

# WAP to check if a number entered by the user is odd or even.

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

# WAP to find the greatest of 3 numbers entered by user.

number1 = int(input("Enter num1: "))
number2 = int(input("Enter num2: "))
number3 = int(input("Enter num3: "))

if number1 > number2 and number1 > number3:
    print("number1 is greater than number2 and number3")
elif number2 > number1 and number2 >number3:
    print("number2 is greater than number1 and number3")
else:
    print("number3 is greater than other two numbers")

# WAP to check if a number is a multiple of 7 or not.

x = int(input("ENter x: "))

if x % 2 == 0:
    print("multiple of 7")
else:
    print("not a multiple of 7")