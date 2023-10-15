#8.Python program to find the sum of the digits of an integer using a while loop.
=int(input("Enter the number"))
total=0
while(num>0):
	digit=num%10
	total=total+digit
	num=num//10
print("sum of the digits =",total)
