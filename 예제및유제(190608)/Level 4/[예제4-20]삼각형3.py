# 출력: 삼각형
# 입력: n
n = int(input("n: "))
for i in range(1, n+1):
    for j in range(1, 2*n):
        if i+j >= n+1 and j-i <= n-1:
            print('*', end='')
        else:
            print(' ', end='')
    print()

