a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def print_even_numbers(arr):
    for i in arr:
        if i % 2 == 0:
            print(i, end=' ')

print_even_numbers(a) # 2 4 6 8 10