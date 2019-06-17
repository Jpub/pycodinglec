# 출력: 마름모
# 입력: n
n = int(input("n: "))
for i in range(1, 2*n):
    for j in range(1, 2*n):
        if n+1 <= i+j <= 3*n-1 and j-i <= n-1 and i-j <= n-1:
            print('*', end='')
        else:
            print(' ', end='')
    print()


