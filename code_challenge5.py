
factorial = 1
number = eval(input("Enter a number to get the factorial -->"))

for i in range(number,0,-1):
    factorial *= i

print("The factorial of",number,"is",factorial)
