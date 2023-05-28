
#WRITE A PROGRAM TO CHANGE CASES OF LETTERS IN PYTHON.
def change(s):
 return str(s).upper(), str(s).lower()
chra = {'a', 'b', 'E', 'f', 'a', 'i', 'o', 'U', 'a'}
result = map(change, chra)
print(list(result))

