#-------------------------------- 1. VARIABLES AND DATATYPES:---------------------------------

name = "Dhruvisha"
age = 19
price = 25.99

print(type(name))
print(type(age))
print(type(price))

a = int("2")
b = 4.25

print(type(a))
sum = a + b
print(sum)

# Input in Python:--

# Write a program to input 2 numbers & print their sum.

a = int(input("Enter number1: "))
b = int(input("Enter number2: "))
sum = a + b
print("Sum of two number is:" ,sum)

# WAP to input side of a square & print its area.

side = float(input("Enter square side : "))

print("area =", side ** 2)

# WAP a program to floating point numbers & print their average.

x = float(input("Enter number 1: "))
y = float(input("Enter number 2: "))
avg = (x + y)/100
print("avarage of two number is =", avg)

# WAP to input 2 int numbers, a and b.
# Print True if a is greater than or equal to b. If not print False.

c = int(input("Enter number1: "))
d = int(input("Enter number2: "))

if c >= b:
    print(True)
else :
    print(False)
