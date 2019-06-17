# 출력: 피보나치수열의 n번째 항
# 입력: n
def f(n):
    if n == 1 or n == 2:
        return 1
    a = 1    # f(1)
    b = 1    # f(2)
    i = 2
    while True:
        c = a+b    # f(n) = f(n-2) + f(n-1)
        i += 1    # 방금 계산한 값이 몇 번째 항인지 갱신
        if i == n:
            break
        a, b = b, c  # 다음 반복에서 c=a+b를 수행할 수 있도록 숫자를 한 칸씩 당김
    return c

n = int(input("n: "))
print(f(n))



