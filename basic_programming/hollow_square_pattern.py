n = 5

for i in range(n):
    for j in range(n):
        # Print stars for the border of the square
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            # Print spaces for the hollow part
            print(" ", end=" ")
    print()