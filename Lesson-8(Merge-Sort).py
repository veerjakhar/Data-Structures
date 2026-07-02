data = [50, 30, 29, 58, 20, 10, 1, 3, 5, 7, 9, 2, 4, 6, 8, 11, 14, 18]
n = len(data)

def merge_sort(data, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(data, low, mid)
        # First Area
        merge_sort(data, mid + 1, high)
        # Second Area
        merge(data, low, mid, high) # - Combines the 2 sorted area's together

def merge(data, low, mid, high):
    c = []
    start1 = low
    start2 = mid + 1
    while start1 <= mid and start2 <= high:
        if data[start1] < data[start2]:
            c.append(data[start1])
            start1 = start1 + 1
        else:
            c.append(data[start2])
            start2 = start2 + 1

    while start1 <= mid:
        c.append(data[start1])
        start1 = start1 + 1
    
    while start2 <= high:
        c.append(data[start2])
        start2 = start2 + 1

    k = 0
    for i in range(low, high + 1):
        data[i] = c[k]
        k += 1

merge_sort(data, 0, n - 1)
print(data)