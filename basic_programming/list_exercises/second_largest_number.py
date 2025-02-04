a = [7, 10, 4, 3, 20, 15]

def find_second_largest(arr):

    if len(arr) < 2:
        return None

    largest = second_largest = float('-inf')

    for number in arr:
        if number > largest:
            second_largest = largest
            largest = number
        elif number > second_largest and number != largest:
            second_largest = number

    return second_largest

print(find_second_largest(a)) # 15