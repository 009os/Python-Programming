
#WRITE A PROGRAM TO FIND SUM OF ALL ELEMENTS IN THE LIST.

list1 = []
n = int(input("Enter the list size "))
add=0
for i in range(0, n):
 item = int(input())

 list1.append(item)
 add=add+item
print("THE User list is : ", list1)
print("ITEMs SUM is : ", (add/n))

