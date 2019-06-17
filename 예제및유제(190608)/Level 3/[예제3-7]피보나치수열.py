# 출력: 피보나치 수열의 n번째 항
# 입력: n
def f(n):
    if n == 1 or n == 2:
        return 1
    return f(n-1)+f(n-2)

n = int(input("n: "))
print(f(n))


