n = 5
for i in range(n):
    # Print leading spaces
    for j in range(i):
        print(" ", end="")
    # Print asterisks
    for j in range(n - i):
        print("* ", end="")
    print()