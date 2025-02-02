def interchange_1_2(arr):
    if len(arr) < 2:
        return arr

    arr[0], arr[-1] = arr[-1], arr[0]
    return arr

arr = [1, 2, 3, 4, 5]
print(interchange_1_2(arr))  # Output: [5, 2, 3, 4, 1]

arr = [0, 1]
print(interchange_1_2(arr))  # Output: [1, 0]

arr = [1]
print(interchange_1_2(arr))  # Output: [1]


def interchange_1_2(arr):
    # Check if the array has at least two elements
    if len(arr) < 2:
        return arr
    
    # Use a temporary variable to swap the first and last elements
    temp = arr[0]
    arr[0] = arr[-1]
    arr[-1] = temp
    
    return arr

arr = [1, 2, 3, 4, 5]
print(interchange_1_2(arr))  # Output: [5, 2, 3, 4, 1]