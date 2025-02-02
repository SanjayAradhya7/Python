def max_numbers(a, b):
    if a>b:
        return a
    else:
        return b

# Example usage
a = 10
b = 20
print(max_numbers(a, b))  # Output: 20

a = -7
b = 1006
print(max_numbers(a, b))  # Output: 20

a = 7
b = 3
print(max(a, b))  # Output: 7

a = 7
b = 2
res = a if a > b else b
print(res)