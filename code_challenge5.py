#Calculate the factorial
import os
print("\nFactorial Calculator")

number = eval(input("\nEnter a number to get the factorial -->"))
os.system('cls')

factorial = 1

for i in range(number,0,-1):
    factorial *= i

print("The factorial of",number,"is",factorial)