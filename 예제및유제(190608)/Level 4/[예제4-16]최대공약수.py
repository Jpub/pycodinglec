a = int(input("a: "))
b = int(input("b: "))
if a > b:
    a, b = b, a    # a가 b보다 작은 값을 갖도록 조정
a_numbers = []    # a의 약수를 저장할 리스트
for i in range(1, int(a**0.5)+1): # [문제4-15]의 코드를 응용
    if a % i == 0:
        a_numbers.append(i)
        a_numbers.append(a//i)
common_divisor = []    # 공약수를 저장할 리스트
for i in a_numbers:
    if b % i == 0:        # i가 a의 약수면서 b의 약수라면
        common_divisor.append(i)  # 공약수 리스트에 추가
print(max(common_divisor))

