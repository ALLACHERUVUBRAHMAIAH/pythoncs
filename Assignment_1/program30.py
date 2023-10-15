a=int(input("Enter the any number ="))
b=int(input("Enter the any number ="))

print("1 - Addition\n2 - Substraction\n3 - Multiplication\n4 - Division\n5 - Floor Division\n6 - Modulo")
option = int(input("Enter one option from the above list:- "))
if option == 1:
   print(f"Addition: {a + b}")
elif option == 2:
   print(f"Substraction: {a - b}")
elif option == 3:
   print(f"Multiplication: {a * b}")
elif option == 4:
   print(f"Division: {a / b}")
elif option == 5:
   print(f"Floor Division: {a // b}")
elif option == 6:
   print(f"Modulo: {a % b}")
