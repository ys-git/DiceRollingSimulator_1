from random import randint

print("\nPress Enter to Roll the dice\n")
x=input()
while (ord('x')==13):
    print(randint(1, 6))
    print("\n\nPress ENTER to Roll the dice again and ESC to end\n")
    x=input()
    if (ord('x')==27):
        break
