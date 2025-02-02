def min_numbers(a, b):
    if a<b:
        return a
    else:   
        return b

# Example usage
a = 10
b = 20
print(min_numbers(a, b))  # Output: 10

a = -7
b = 1006
print(min(a, b))  # Output: -7

a = 7   
b = 3
res = a if a<b else b
print(res)  # Output: 3