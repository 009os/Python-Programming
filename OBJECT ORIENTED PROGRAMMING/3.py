

#Create a Vehicle class with max_speed and mileage instance attributes as: 
#class Vehicle: 
 #def __init__(self, name, max_speed, mileage): 
 #self.name = name 
 #self.max_speed = max_speed 
 #self.mileage = mileage #
#Instantiate an object of this class and print max_speed and mileage member
class vehicle:
 def __init__(self, name, max_speed, mileage):
 self.name = name
 self.max_speed = max_speed
 self.mileage = mileage
 print('Name = ',self.name,'| speed = ',self.max_speed,'| mileage = ',self.mileage)
s = vehicle('Fortuner',200,'10kmpl')
s = vehicle('rolls royce',250,'9.8kmpl')

