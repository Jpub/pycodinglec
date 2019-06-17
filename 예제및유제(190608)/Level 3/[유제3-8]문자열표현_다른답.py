# 출력: 구구단 중 한 단
# 입력: 단 수
n = int(input("몇 단?: "))
i = 1
while i < 10:
    print("%d x %d = %d" % (n, i, n*i))
    i = i + 1

