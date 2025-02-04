a = [7, 10, 4, 3, 20, 15]

def find_third_largest(arr):

    if len(arr) < 3:
        return None

    largest = second_largest = third_largest = float('-inf')

    for number in arr:
        if number > largest:
            third_largest =  second_largest
            second_largest = largest
            largest = number
        elif number > second_largest and number != largest:
            third_largest = second_largest
            second_largest = number
        elif number > third_largest and number != largest and number != second_largest:
            third_largest = number

    return third_largest

print(find_third_largest(a))