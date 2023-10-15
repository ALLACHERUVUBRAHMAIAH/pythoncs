#16.Python program to display the sum of n numbers using a list.
list = [1, 2, 3, 5, 6, 7, 8, 9, 10] 
sum = 0
for ele in range(0, len(list)):
	sum = sum + list[ele]
print("Sum of elements in list= ", sum)
