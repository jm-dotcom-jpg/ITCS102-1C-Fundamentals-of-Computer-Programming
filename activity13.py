
#Ask the user to input 10 numbers.
#After get the summation of all the numbers provided.

sum = 0
for x in range(1,11,1):
    print(x)
    number = eval(input("Enter the number that you want to sum -->"))
    sum += number

print("\n\tThe sum of all the given numbers is",sum)