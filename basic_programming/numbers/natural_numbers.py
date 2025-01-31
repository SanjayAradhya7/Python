n = 5
for i in range(1, n+1):
    sum = 0
    for j in range(1, i+1):
        print(j, end = " ")
        sum += j
        if j < i:
            print("+", end = " ")
    print(f"= {sum}")

# Output
# 1 = 1
# 1 + 2 = 3
# 1 + 2 + 3 = 6
# 1 + 2 + 3 + 4 = 10
# 1 + 2 + 3 + 4 + 5 = 15
