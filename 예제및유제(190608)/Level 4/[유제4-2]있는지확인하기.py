# 출력: 숫자의 인덱스 또는 ValueError
# 입력: 숫자 묶음과 숫자 하나
numbers = input("정수 묶음: ").split()
number = input("찾을 정수: ")
idx = -1
for i in range(len(numbers)):
    if numbers[i] == number:
        idx = i
        break
if idx == -1:
    raise ValueError
else:
    print("인덱스:", idx)


