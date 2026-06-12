#data = [1,8,6,2,7,3,9,5,4]
data = list(map(int, input("Enter the numbers: ").split()))

key = int(input("Enter the number wanted to be found: "))

#Linear Search
for i in range(0, len(data)):
    #print(data[i]) 
    if key == data[i]:
        print("^ Number found")

for num in data:
    if num == key:
        print("The number has been found")

#Binary Search --> Method 1
def binary(data, key, low, high):
    mid = (low + high)//2
    if low <= high:
        if data[mid] == key:
            return mid
        elif data[mid] < key:
            return binary(data, key, mid + 1, high)
        elif data[mid] > key:
            return binary(data, key, low, mid - 1)
    else:
        return -1

print("Found in the #{} place".format(binary(data, key, 0, len(data)) + 1))

#Binary Search --> Method 2

start = 0
end = len(data) - 1
flag = False

while start <= end:
    mid = (start + end)//2
    if data[mid] == key:
        print("FOUND")
        flag = True
        break
    elif data[mid] > key:
        end = mid - 1
    elif data[mid] < key:
        start = mid + 1
    
if flag == False:
    print("The number (key) was not able to be found in the data given")
