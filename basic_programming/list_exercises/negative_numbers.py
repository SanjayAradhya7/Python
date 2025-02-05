a = [1, -7, 9, 0, -2, 3, 4, 5, -6]

def print_positive_numbers(arr):
    for i in arr:
        if i < 0 :
            print(i, end=' ')

print_positive_numbers(a) # -7 -2 -6