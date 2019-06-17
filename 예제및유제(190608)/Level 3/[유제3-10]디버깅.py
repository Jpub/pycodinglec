def f(n):
    if n == 1 or n == 2:
        return 1
    a = 1
    b = 1
    i = 2
    while True:
        c = a+b
        i += 1
        a, b = b, c
        if i == n:
            return c

n = int(input("n: "))
print(f(n))
