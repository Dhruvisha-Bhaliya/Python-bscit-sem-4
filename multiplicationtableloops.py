# 1.Write a python program to print table of n. Do it using three types of loops.
# Use scanner to take input of n from user.

number = int(input("Enter number: "))
print("The Multiplication Table of: ",number)
for count in range(1,11):
    print(number,'x',count,'=',number*count)



