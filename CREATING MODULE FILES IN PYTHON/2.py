#MODULE FILE :-
44
import functools
def mult(a,b):
 return a*b
def sum(a,b):
 return a+b
def sub(a,b):
 return a-b
def fact(a):
 if a==1:return 1
 return a*fact(a-1)
def avg(ls):
 a=functools.reduce(lambda a,b:a+b,ls)
 a=a/len(ls)
 return a