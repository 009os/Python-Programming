
#WRITE A PROGRAM TO CHECK WHETHER A GIVEN IS ARMSTRONG NUMBER OR NOT .

num = int(input("Enter a number: "))
sum = 0
t = num
while t > 0:
 n = t % 10
 sum = sum + n ** 3
 t =t// 10
if num == sum:
 print(num,"is an Armstrong number")
else:
 print(num,"is not an Armstrong number")

