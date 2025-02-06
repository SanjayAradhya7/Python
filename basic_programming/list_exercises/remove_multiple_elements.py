a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

remove = [20, 60, 100]
res = []
for i in a:
    if i not in remove:
        res.append(i)

print(res) # [10, 30, 40, 50, 70, 80, 90]

