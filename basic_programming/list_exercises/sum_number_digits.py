a = [123, 456, 789]
sum_digits_list = []

for number in a:
    sum_digits = 0
    while number > 0:
        digit = number % 10
        sum_digits += digit
        number = number // 10
    sum_digits_list.append(sum_digits)

print(sum_digits_list) 

# Output: [6, 15, 24]