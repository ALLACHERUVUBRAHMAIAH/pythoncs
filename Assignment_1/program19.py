#19.Python program to find the odd numbers in an array .
numbers = [1,2,3,4,5,6,7,8,9,10]
count = 0
for i in range(len(numbers)):
    if(numbers[i]%2!=0):
        count = count+1
print("The number of odd numbers in the list are: ", count)
