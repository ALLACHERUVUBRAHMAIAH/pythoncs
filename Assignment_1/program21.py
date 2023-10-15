#21.Python program to insert a number to any position in a list .
numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers)
x = int(input("Enter the number to be inserted: "))
y = int(input("Enter the position: "))
numbers.insert(y,x)
print(numbers)

