
#Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes. • 
#Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the area of 
#the rectangle. • Create a method display() that display the length, width, perimeter and area of an object created 
#using an instantiation on rectangle class. • Create a cuboid child class inheritin#g from the Rectangle class and with a 
#height attribute and another Volume() method to calculate the volume of the cuboid
class rectangle:
 def __init__(self,length,width):
 self.length=length
 self.width=width
 def perimeter(self):
 return 2*(self.length + self.width)
 def Area(self):
 return self.length*self.width 
 def display(self):
 print("The length of rectangle is: ", self.length)
 print("The width of rectangle is: ", self.width)
 print("The perimeter of rectangle is: ", self.perimeter())
 print("The area of rectangle is: ", self.Area())
 class cuboid(rectangle):
 def __init__(self, length, width , height):
 rectangle.__init__(self, length, width)
 self.height = height
 def volume(self):
 return self.length*self.width*self.height
r= rectangle(7 , 5)
r.display()
c = cuboid(7 , 5 , 2)
print("the volume is: " , c.volume())

