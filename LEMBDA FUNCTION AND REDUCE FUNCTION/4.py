
#WRITE A PROGRAM TO FIND SMALLEST NUMBER IN A LIST.
from functools import reduce
def smallest(a,b):
 if(a<b):
 c=a
 else:
 smallest(a,b)
 return c 
L = [1,2,3,4,5,6]

a=reduce(smallest,L)
print(a)
