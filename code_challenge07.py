#Odd number accumulator

sum = 0
for i in range(1,11,1):
    number = eval(input(f"Enter a number {i}:"))
    
    if number % 2 == 1:
        sum += number

print("\nSum of all numbers:",sum)
