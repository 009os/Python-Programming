

#WRITE A PROGRAM TO FIND NUMBERS IN LIST DIVISIBLE BY 5 USING LAMBDA FUNCTION.

nums = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
print("Orginal list:")
print(nums) 
result = list(filter(lambda x: (x % 5 ==0), nums)) 
print("\nNumbers of the above list divisible by 5 :")
print(result)

