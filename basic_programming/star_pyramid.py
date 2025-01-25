n = 5
for i in range(n):
    # Print Leading Spaces
    for j in range(n-i):
        print(" ", end="")
    # Print Asterisks
    for k in range(i+1):
        print("* ", end="")
    print()