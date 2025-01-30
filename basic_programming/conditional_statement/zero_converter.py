def neg(n):
    if n == 0:
        print("already Zero")
        return
    while n <= -1:
        print(n, end = " ")
        n += 1
    print()

def pos(n):
    if n == 0:
        print("already Zero")
        return
    while n >= 1:
        print(n, end = " ")
        n -= 1
    print()

# Example usage
neg(-5)  # Output: -5 -4 -3 -2 -1
neg(-10) # Output: -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
pos(5)   # Output: 5 4 3 2 1
pos(10)  # Output: 10 9 8 7 6 5 4 3 2 1
pos(0)   # Output: already Zero
neg(0)   # Output: already Zero

