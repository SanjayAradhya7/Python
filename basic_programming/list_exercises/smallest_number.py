a = [98, 23, 45, 67, 12, 89, 34, 56, 78, 90]

smallest = min(a)
print(smallest)

#Brute force
a = [98, 23, 45, 67, 12, 89, 34, 56, 78, 90]
smallest = a[0]
for i in a:
    if i < smallest:
        smallest = i
print(smallest)

#Using Sorting

a = [8, 3, 5, 1, 9, 12]
a.sort()
smallest = a[0]
print(smallest)