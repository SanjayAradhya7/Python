a = [33, 67, 80, 33, 67, 33, 33, 33]

s = set(a)
dup = []

for i in a:
    if i in s:
        dup.append(i)
    else:
        s.add(i)
print(s)

# Output: {33, 67, 80}

a = [1, 6, 5, 1, 4, 5, 4]

a = list(set(a))
print(a)