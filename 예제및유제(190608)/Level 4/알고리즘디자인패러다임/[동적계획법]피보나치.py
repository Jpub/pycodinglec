fibonacci = {}  # 딕셔너리

def f(n):
    if n == 1 or n == 2:
        fibonacci[n] = 1
        return fibonacci[n]

    a = fibonacci.get(n-1)    # a: 직전항. 없으면 None이 반환됨
    if not a:
        fibonacci[n-1] = f(n-1)  # 직전항이 저장되어있지 않다면, 구해서 딕셔너리에 저장.

    b = fibonacci.get(n-2)    # b: 전전항. 없으면 None이 반환됨
    if not b:
        fibonacci[n-2] = f(n-2)  # 직전항이 저장되어있지 않다면, 구해서 딕셔너리에 저장.

    return fibonacci[n-1]+fibonacci[n-2]  # 딕셔너리에 저장된 전항과 전전항의 합을 반환

n = int(input("n: "))
print(f(n))

############################################################
