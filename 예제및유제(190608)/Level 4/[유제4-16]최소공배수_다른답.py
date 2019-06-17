def gcd(a, b):
    if b % a == 0:
        return a
    return gcd(b % a, a)

a = int(input("a: "))
b = int(input("b: "))
print(int(a*b/gcd(a, b)))
