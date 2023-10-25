from datetime import date
class Student_details:
	def __init__(self,Name,age):
		
		self.Name=Name
		self.age=age
	
	def get_Name(self):
		print("Name is =",self.Name)
		
	sub1=int(input("Enter marks of the first subject: "))
	sub2=int(input("Enter marks of the second subject: "))
	sub3=int(input("Enter marks of the third subject: "))
	sub4=int(input("Enter marks of the fourth subject: "))
	sub5=int(input("Enter marks of the fifth subject: "))
	avg=(sub1+sub2+sub3+sub4+sub4)/5
	if(avg>=90):
		print("Grade: A")
	elif(avg>=80&avg<90):
		print("Grade: B")
	elif(avg>=70&avg<80):
		print("Grade: C")
	elif(avg>=60&avg<70):
		print("Grade: D")
	else:
    		print("Grade: F")
	def get_age(self):
		print("age is =",self.age)
		
S1=Student_details("ALLACHERUVU BRAHMAIAH",22)
S1.get_Name()
S1.get_age()

 

