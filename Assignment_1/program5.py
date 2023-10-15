#5.Python program to check whether the given integer is a multiple of both 5 and 7.
num=int(input("Enter any number"))
if num%7==0:
	if num%5==0:
		print("The number is divisible by 5,7.")
else:
	print("The number is not divisible by 5,7.")
