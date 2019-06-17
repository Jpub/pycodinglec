n = int(input("n: "))
for i in range(1, n+1):
    for j in range(1, i):
        print(' ', end='')
    for j in range(1, 2*(n-i+1)):
        print('*', end='')
    print()

#
