for i in range(1,11,1):
    for j in range(10,i,-1):
        print(" ", end=" ")
    for f in range(1, i, 1):
        print("*", end=" ")
    for v in range(i - 1,1,-1):
        print("*", end=" ")
    print()

for i in range(9, 0, -1):
    for j in range(10, i, -1):
        print(" ", end=" ")
    for f in range(1, i):
        print("*", end=" ")
    for v in range(i - 1, 1, -1):
        print("*", end=" ")
    print()
