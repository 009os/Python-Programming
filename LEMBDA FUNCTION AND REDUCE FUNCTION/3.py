
#WRITE A PROGRAM TO ADD AND SUBSTRACT TWO LIST.
result = map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6])
result1 = map(lambda x, y: x - y, [1, 2, 3], [4, 5, 6])
print("\nResult: after adding two list")
print(list(result))
print("\nResult: after substracting two list")
print(list(result1))
