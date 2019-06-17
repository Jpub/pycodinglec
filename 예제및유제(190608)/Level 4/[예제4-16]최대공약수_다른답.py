def gcd(a, b):
    if b % a == 0:
        return a
    return gcd(b % a, a)


a = int(input("a: "))
b = int(input("b: "))
if a > b:
    a, b = b, a    # a가 b보다 작은 값을 갖도록 조정

print(gcd(a, b))

#
