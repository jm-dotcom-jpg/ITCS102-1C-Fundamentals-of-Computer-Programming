from getpass import getpass

username = 'helloworld@gmail.com'
password = 'hello_how_are_you'

u = input("Please Enter Your Username/Email:")
p = getpass("Please Enter Your Password:")

if (u == username ) and ( p == password):
	print("Access granted!")
else:
	print("Incorrect Username/Password")