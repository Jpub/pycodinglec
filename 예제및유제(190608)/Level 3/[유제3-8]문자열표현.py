# 출력: 구구단 중 한 단
# 입력: 단 수
n = int(input("몇 단?: "))
for i in range(1, 10):
    print("%d x %d = %d" % (n, i, n*i))

