print("\nGreetings!! from Transportation Inc.")
name = input("\nWhat is your name?:") 
fare = eval(input("Enter the amount of your fare fee:"))
student = input("Are you a student?:Yes/No:")
discount = fare * 0.2

if student.lower().strip() == 'yes' :
	fare = fare - discount
	print("Hello", name, "here is your discounted fare",fare)
else:
	print("Apologies" ,name, "but you are not eligible of the student discount.")

	