
#WRITE A PROGRAM TO CALCULATE CI.

print("ENTER PRINCIPLE,RATE AND TIME")
p=int(input())
r=int(input())
t=int(input())
CI=p*(1+(r/100))**t
print("THE CI is : ",CI)
