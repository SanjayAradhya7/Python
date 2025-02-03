a = [77, 33, 44, 11, 22, 55, 66]

largest = max(a)
print(largest)


#Brute force
a = [77, 33, 44, 11, 22, 55, 66]
largest = a[0]
for i in a:
    if i > largest:
        largest = i
print(largest)

#Using Sorting
a = [77, 33, 44, 11, 22, 55, 66]
a.sort()
largest = a[-1]
print(largest)