def printInDecreasing(x):
    while x >= 0:
        print(x, end=" ")
        x -= 1
    print()

# Example usage
printInDecreasing(5)  # Output: 5 4 3 2 1 0
printInDecreasing(10) # Output: 10 9 8 7 6 5 4 3 2 1 0