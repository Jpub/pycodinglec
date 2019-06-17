count = [0, 1, 2, 4]
n = int(input("계단 수: "))
if n <= 3:
    print(count[n])
else:
    for i in range(4, n+1):
        count.append(count[i-1]+count[i-2]+count[i-3])
    print(count[n])

