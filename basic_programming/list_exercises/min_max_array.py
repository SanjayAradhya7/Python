def find_min_max(arr):
    if not arr:
        return None, None

    min_element = arr[0]
    max_element = arr[0]

    for num in arr:
        if num < min_element:
            min_element = num
        if num > max_element:
            max_element = num

    return min_element, max_element

# Example usage
arr = [1, 2, 3, 4, 5]
print(find_min_max(arr))  # Output: (1, 5)

arr = [80, 20, 30, 40, 50]
print(find_min_max(arr))  # Output: (20, 80)

arr = []
print(find_min_max(arr))  # Output: (None, None)