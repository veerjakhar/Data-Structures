data = [3, 4, 8, 2, 6, 5, 7, 9, 1]
print(data)
n = len(data)
'''
for i in range(n):
    for j in range(i, n):
        if data[i] < data[j]:
            data[i], data[j] = data[j], data[i]
'''

for i in range(n):
    for j in range(i, n):
        if data[i] > data[j]:
            data[i], data[j] = data[j], data[i]

print(data)
