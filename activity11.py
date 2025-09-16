temp = float(input("\nEnter temperature -->"))

if temp >= 1 and temp <= 20:
    print("\nYou need to wear jacket.")

elif temp >= 21 and temp <= 30:
    print("\nYou can wear your usual clothes...")

elif temp >= 31 and temp <= 37:
    print("\nIt's luke warm huh")

elif temp >= 38 and temp <= 45:
    print("\nYou need to hydrate more...")\
    
elif temp >= 45  and temp <= 50:
    print("\nPut your sunblock on!!")

elif temp > 50:
    print("\nWarning!! It's Dangerous!!")

else:
    print("\nInvalid Input")