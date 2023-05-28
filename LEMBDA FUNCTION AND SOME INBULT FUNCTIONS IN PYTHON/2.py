
#WRITE A PROGRAM TO FIND SQAURE OF NUMBERS BY LAMBDA FUNCTION.

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list of integers:")
print(nums)
print("\nSqaure every number of the said list:")
sqaure_nums = list(map(lambda x: x ** 2, nums))
28
print(sqaure_nums)
