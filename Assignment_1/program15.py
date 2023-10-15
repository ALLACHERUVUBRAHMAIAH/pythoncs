#15.Python program to find the factorial of a number using recursion .
n=int(input("Enter number:"))
factorial=1
while(n>0):
    factorial=factorial*n
    n=n-1
print("Factorial of the number is: ")
print(factorial)
