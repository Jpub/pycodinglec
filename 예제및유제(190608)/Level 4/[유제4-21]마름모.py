# 출력: 마름모
# 입력: n
n = int(input("n: "))
for i in range(1, 2*n):
    for j in range(1, 2*n):
        if i+j <= n+1 or i+j >= 3*n-1 or j-i >= n-1 or i-j >= n-1:
            print('*', end='')
        else:
            print(' ', end='')
    print()

