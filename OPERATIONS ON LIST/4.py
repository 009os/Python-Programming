

#WRITE A PROGRAM TO PERFORM LCM OF 2 NUMBERS.

a=int(input())
b=int(input())
if (a > b):
 c = a
else:
 c = b
while(True):
 if(c% a == 0 and c % b == 0):
 print('The LCM of',a,'and',b,'is',c)
 break
 c += 1

