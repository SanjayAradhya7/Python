a = [1, 2, 3, 4, 5]

total = sum(a)
print(total)

average = sum(a) / len(a)
print(average)

#Brute Force
a = [1, 2, 3, 4, 5]
sum = 0
length = 0
for i in a:
    sum += i
    length += 1
average = sum / length
print(sum, average)
