#Multiplication Table Maker

print("\nCreate your own multiplication Table.")
number = eval(input("\nEnter a number -->"))
print("Multiplication Number for", number)

for  i in range(1,11):
    print(number,f"x {i} =",number * i)