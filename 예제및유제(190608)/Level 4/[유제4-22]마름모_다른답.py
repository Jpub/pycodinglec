n = int(input("n: "))
for i in range(1, 2*n):
    for j in range(1, 2*n):
        if abs(n-i)+abs(n-j) >= n-1:  # abs()는 절대값을 구하는 함수
            print('*', end='')
        else:
            print(' ', end='')
    print()

