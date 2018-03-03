import sys

from random import randint
print("\nPress 1 to Roll the dice\n")
x=input()
while x=='1':
    print(randint(1, 6))
    while x=='1' or x=='0':
        print("\n\nPress 1 to Roll the dice again and 0 to end\n")
        x = input()
        if ('x' == '0'):
            sys.exit1
        else:
            print("Please Enter the relevent input")

