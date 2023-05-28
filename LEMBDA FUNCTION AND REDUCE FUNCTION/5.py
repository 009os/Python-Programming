
#WRITE A PROGRAM TO FIND AVEARAGE OF ALL NUMBERS IN A LIST.

from functools import reduce
def add(a,b):
 return a+b
L = [1,2,3,4,5]
a=reduce(add,L)
print(a/len(L))