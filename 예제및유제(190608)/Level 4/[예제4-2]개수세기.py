# 출력: 숫자 포함 횟수
# 입력: 숫자 묶음과 숫자 하나

numbers = input("정수 묶음: ").split()
number = input("찾을 정수: ")
n = 0
for i in numbers:
    if i == number:
        n += 1
print("포함:", n)




