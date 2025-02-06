a = [(1, 2), (), (3, 4), (), (5,)]

res = []
for i in a:
    if i:
        res.append(i)

print(res) # [(1, 2), (3, 4), (5,)]