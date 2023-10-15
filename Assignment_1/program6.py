#6.Python program to display the given integer in a reverse manner .
num=int(input("Enter the any number"))
reverse=0
while num%10:
	reminder=num%10
	reverse=(reverse*10)+reminder
	num=num//10
print(reverse)
	
