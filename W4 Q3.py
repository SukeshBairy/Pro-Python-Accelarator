def division(a,b):
	try:
		print("Result of Division: " + str(a/b))
	except(ZeroDivisionError):
		print("You have divided a number by zero, which is not allowed.")
	except(ValueError):
		print("You must enter integer value")

a = int(input("Enter numerator number: "))
b = int(input("Enter denominator number: "))
division(a,b)