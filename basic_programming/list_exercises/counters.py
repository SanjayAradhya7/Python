#Using count()
a = [1, 3, 2, 6, 3, 2, 8, 2, 9, 2, 7, 3]

print(a.count(2))
print(a.count(3))

#Using a Loop
a = [1, 3, 2, 6, 3, 2, 8, 2, 9, 2, 7, 3]
count = 0
for i in a:
    if i == 2:
        count += 1
print(count)