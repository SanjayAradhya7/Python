a  = [47, 98, 3, 1, 76, 98, 3]

res = list(set(a))
print(res)


a = [1, 2, 2, 3, 5, 5, 7]

unique = []

for i in a:
    if i not in unique:
        unique.append(i)
print(unique)
