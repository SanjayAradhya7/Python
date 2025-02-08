a = [1, 2, 3, 4, 1, 2, 7, 8, 4]

s = set()
dup = []

for i in a:
    if i in s:
        dup.append(i)
    else:
        s.add(i)
print(dup)

# Output: [1, 2, 4]


