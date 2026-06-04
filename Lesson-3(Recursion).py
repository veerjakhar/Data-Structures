# Fib(n) = Fib(n - 1) + Fib(n - 2)

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(0))

# fac(n) = fac(n-1)*n

def fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fac(n - 1) * n

print(fac(2))

def fir(n):
    if n == 1 or n == 0:
        return n
    else:
        return n + fir(n - 1)

print(fir(15))

def pow(x, y):
    if y == 1:
        return x
    else:
        if y%2 == 0:
            return pow(x, y//2) * pow(x, y//2)
        else:
            return(x * pow(x, y//2) * pow(x, y//2))

print(pow(1009090099009, 2))