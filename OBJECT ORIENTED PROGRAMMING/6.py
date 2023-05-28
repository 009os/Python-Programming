

#WRITE A PROGRAM TO PERFORM EXCEPTION HANDLING IN PYTHON
#NAME ERROR :-
def fun(a):
 print("Value of b = ", b)
try:
 fun(3)
except NameError:
 print("NameError Occurred and Handled")
 
#TYPE ERROR :-
x = "hello"
try:
39
 if not type(x) is int:
 raise TypeError
except TypeError:
 print("Only integers are allowed")
#VALUE ERROR AND ATTRIBUTE ERROR :-
try:
 x=int(input('enter a number : '))
 if 100/x > 1:
 raise AttributeError
 else:
 print('saved')
except AttributeError:
 print('ATTRIBUTE ERROR OCCURED AND HANDLED')
except valueError:
 print('cannot convert string to number')

