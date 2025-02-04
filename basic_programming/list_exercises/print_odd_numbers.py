a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def print_odd_numbers(arr):
    for i in arr:
        if i % 2 != 0:
            print(i, end=' ')

print_odd_numbers(a) # 1 3 5 7 9