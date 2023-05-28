#WRITE A PROGRAM TO FIND FACTORIAL OF A NUMBER.

a=int(input("ENTER A NUMBER YOU WANT IT's FACTORIAL : "))
fact=1
if(a==1):
 print(1)
else:
 while a!=1:
 fact=fact*a
 a=a-1
print(fact)

