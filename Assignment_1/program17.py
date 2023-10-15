#17.Python program to implement linear search .
numbers = [1,2,3,4,5,6,7,8,9,10]
x = int(input("Enter the number to be found out: "))
for i in range(len(numbers)):
    if (x==numbers[i]):
        print("Successful search, the element is found at position", i)
        break
if(x==0):
    print("Oops! Search unsuccessful")
