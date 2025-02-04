a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def count_even_odd(arr):
    even_count = 0
    odd_count = 0
    for i in arr:
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count

even_count, odd_count = count_even_odd(a)
print(f"Even numbers are: {even_count}")
print(f"Odd numbers are: {odd_count}")