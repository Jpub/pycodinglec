from math import factorial as fa
n = int(input("n: "))
r = int(input("r: "))
print(fa(n)//(fa(r)*fa(n-r)))

