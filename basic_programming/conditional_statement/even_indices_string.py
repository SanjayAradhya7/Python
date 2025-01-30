def stringJumper(str):
    for i in range(len(str)):
        if i%2 == 0:
            print(str[i], end = " ")
    print()

# Example usage
stringJumper("hello")
stringJumper("world")