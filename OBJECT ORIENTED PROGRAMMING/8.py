

#PROGRAM TO TAKE STUDENT DATA AS INPUT AND PERFROM EXCEPTION HANDLING IF AGE > 100 
#or GENDER IS OTHERTHAN MALE OR FEMALE.


class Student:
 def init(self, name, age, gender, dob):
 self.name = name
 self.age = age
 self.gender = gender
 self.dob = dob
class AgeError(Exception):
 pass
class GenderError(Exception):
 pass
student_list = []
while True:
 print("1. Add Student Record 2. Show Student Record 3. Exit")
 choice = int(input("Enter your choice: "))
 if choice == 1:
 try:
 name = input("PLEASE Enter student name: ")
 age = int(input("PLEASE Enter student age: "))
 if age < 0 or age > 100:
 raise AgeError
 gender = input("PLEASE Enter student gender: ")
 if gender != 'male' and gender != 'female':
 raise GenderError
 dob = input("PLEASE Enter student date of birth: ")
 student = Student(name, age, gender, dob)
 student_list.append(student)
 print("Student Record Added Successfully!!")
 except AgeError:

 print("Invalid Age!!")
 except GenderError:
 print("Invalid Gender!!")
 elif choice == 2:
 for student in student_list:
 print("Name: {} Age: {} Gender: {} DOB: {}".format(student.name, student.age, student.gender, 
student.dob))
 elif choice == 3:
 break
 else:
 print("Invalid Choice!!"