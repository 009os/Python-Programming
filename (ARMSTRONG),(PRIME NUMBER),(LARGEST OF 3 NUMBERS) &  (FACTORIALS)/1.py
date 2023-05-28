
# WRITE A PROGRAM TO FIND LARGEST OF 3 NUMBERS.

print("ENTER 3 NUMBERS \n")
a = int(input())
b = int(input())
c = int(input())
if (a > b):
    if (a > c):
    print("A is largest ")
    else:
    print("C is largest")
else:
    if (b > c):
        print("B is largest")
    else:
        print("C is largest")
