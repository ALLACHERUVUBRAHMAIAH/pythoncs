#22.Python program to delete an element from a list by index .
numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers)
x = int(input("Enter the position of number to be deleted: "))
numbers.pop(x)
print(numbers)

