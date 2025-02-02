def union_two_arrays(a, b):
    union_list = []

    for i in range(len(a)):
        if a[i] not in union_list:
            union_list.append(a[i])

    for j in range(len(b)):
        if b[j] not in union_list:
            union_list.append(b[j])

    return len(union_list)

a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
print(union_two_arrays(a, b)) # Output: 5

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
print(union_two_arrays(a, b))  # Output: 10

a = [1, 2, 1, 1, 2]
b = [2, 2, 1, 2, 1] 
print(union_two_arrays(a, b)) # Output: 2