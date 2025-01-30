def printIncreasingPower(x):
    i = 1
    while (i**2) <= x:
        print(i**2, end = " ")
        i += 1
    print()

# Example usage
printIncreasingPower(5)
printIncreasingPower(10)
printIncreasingPower(25)