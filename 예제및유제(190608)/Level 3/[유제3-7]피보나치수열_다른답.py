def f(n):
    fibonacci = [0, 1]
    for i in range(2, n+1):
        fibonacci += [fibonacci[i-1]+fibonacci[i-2]]
    return fibonacci[n]

n = int(input("n: "))
print(f(n))

