import sys

from random import randint
def inp():
    x=input()
    return x


print("\nPress 1 to Roll the dice\n")
l=inp()

if l!='1' or l!='0':
    print("Please enter the relevant input")


while l=='1' or l=='0':
    if l=='1':
        print(randint(1, 6))
        print("\n\nPress 1 to Roll the dice again and 0 to end •\n")
        l = inp()
    elif ('l' == '0'):
        sys.exit1
    if l!='1' or l!='0' :
        print("Please enter the relevant input")
        l = inp()








