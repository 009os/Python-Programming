
#1. Create a module calculation.py with three functions sum of two numbers, 
#multiplication of two numbers and subtraction of two numbers. Import 
#summation function from module and call.
#2. Create a module calculation.py with three functions sum of two numbers, 
#multiplication of two numbers and subtraction of two numbers. Import all 
#functions from module and call.
#3. Create a module calculation.py with three functions sum of two numbers, 
#multiplication of two numbers and subtraction of two numbers. Import 
#module by renaming as cal and call the functions.
#4. Create a module factorial.py. Import factorial function from module and call 
#to calculate the factorial of a number given by user.
#5. Create a module avg.py. Import average function from module and call to 
#calculate the average of a list.

import calculation as cal
a=2
b=3
print(cal.mult(a,b))
print(cal.sub(a,b))
print(cal.sum(a,b))
print(cal.fact(6))
ls=[1,2,3,4,5,6,7,8,9,10]
print(cal.avg(ls))
