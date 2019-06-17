# 출력: 구구단 중 한 단
# 입력: 단 수(반복)
while True:
    n = input("몇 단?: ")
    if n == 'x':
        break
    else:
        n = int(n)
        for i in range(1, 10):
            print(n, 'x', i, '=', n*i)

