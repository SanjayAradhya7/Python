a = [6, -44, 8, -3, 0, 0, 9, 10, -2]

def count_positive_negative(arr):
    pos_count = 0
    neg_count = 0
    for i in arr:
        if i > 0:
            pos_count += 1
        elif i < 0:
            neg_count += 1

    return pos_count, neg_count

pos_count, neg_count = count_positive_negative(a)
print(f"Positive numbers are: {pos_count}")
print(f"Negative numbers are: {neg_count}")