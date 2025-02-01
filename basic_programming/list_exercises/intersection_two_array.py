def intersection_two_arrays(a, b):
    intersection_list = []

    for element in a:
        if element in b and element not in intersection_list:
            intersection_list.append(element)

    return (intersection_list)

a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
print(intersection_two_arrays(a, b)) # Output: [1, 2, 3, 4, 5]

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
print(intersection_two_arrays(a, b))  # Output: []