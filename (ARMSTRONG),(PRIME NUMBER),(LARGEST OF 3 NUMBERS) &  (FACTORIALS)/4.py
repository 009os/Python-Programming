#WRITE A PROGRAM TO PRINT A PRIME NUMBERS BETWEEN A RANGE.

lower=int(input("ENTER LOWER LIMIT "))
upper = int(input("ENTER END LIMIT "))
print("Prime numbers between ",lower, "and", upper, "are:")
for i in range(lower, upper + 1):
 if i > 1:
 for j in range(2, i):
 if (i % j) == 0:
 break
 else:
 print(i)
