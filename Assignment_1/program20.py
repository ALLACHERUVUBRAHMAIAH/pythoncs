#20.Python program to find the largest number in a list without using built -in functions.
numbers = [5,25,60,30,12,45,20,5]
largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
print("The largest number in the list is:", largest)
