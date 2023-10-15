#23.Python program to check whether a string is palindrome or not .
string=input("Enter string:")
if(string==string[::-1]):
      print("The string is a palindrome")
else:
      print("The string isn't a palindrome")
