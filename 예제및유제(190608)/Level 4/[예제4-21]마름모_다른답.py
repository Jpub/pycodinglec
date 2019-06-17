n = int(input("n: "))
for i in range(1, 2*n):
    for j in range(1, 2*n):
        if abs(n-i)+abs(n-j) < n:  # abs()는 절대값을 반환
            print('*', end='')
        else:
            print(' ', end='')
    print()

