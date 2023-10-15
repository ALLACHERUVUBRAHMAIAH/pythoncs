#3.Python program to find the product of a set of real numbers .
count= int(input("Enter real numbers count ="))
product=1
for i in range(count):
	val =float(input("Enter real Numbers ="))
	product=product*val
print("real numbers is =",product)
