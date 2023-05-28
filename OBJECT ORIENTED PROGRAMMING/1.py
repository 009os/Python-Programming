#Write a python program to display the operator level polymorphism for + operator.

class A:
 def __init__(self, a):
 self.a = a
 def __add__(self, o):
 return self.a + o.a
ob1 = A(1)
ob2 = A(2)
print(ob1 + ob2)
