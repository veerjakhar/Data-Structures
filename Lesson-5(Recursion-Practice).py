x = int(input("What is the number that you want to be turned into Square Root:"))

def ok (x):
    high = x
    low = 0
    while low <= high:
        mid = (low + high)//2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            low = mid + 1
        elif mid * mid > x:
            high = mid - 1
    return high

print(ok(x))



