n = int(input("n: "))
numbers = []    # 약수를 저장할 리스트
for i in range(1, int(n**0.5)+1):    # int(n**0.5)+1: n의 제곱근보다 작지 않은 정수
    if n % i == 0:
        numbers.append(i)
        numbers.append(n//i)
for i in set(numbers):
    print(i, end=' ')

