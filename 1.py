
#WRITE A PROGRAM TO FIND CUBE OF NUMBERS BY LAMBDA FUNCTION.

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list of integers:")
print(nums)
print("\nCube every number of the said list:")
cube_nums = list(map(lambda x: x ** 3, nums))
print(cube_nums)

