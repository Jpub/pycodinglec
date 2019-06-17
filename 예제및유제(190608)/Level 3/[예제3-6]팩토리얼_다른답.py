def factorial(n, i=1):
    if i == n:
        return n
    return i*factorial(n, i+1)

print(factorial(5))


#
