n = int(input("n: "))
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print('*', end='')
    print()


