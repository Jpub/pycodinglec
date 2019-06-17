def factorial(n):
    a = n*factorial(n-1)
    if n == 0: return 1
    return a

print(factorial(5))



