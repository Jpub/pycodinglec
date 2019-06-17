# 출력: 가장 큰 숫자
# 입력: 숫자 여러 개

numbers = input("여러 개의 숫자 입력: ")
numbers = [int(i) for i in numbers.split()]
max_number = numbers[0]
for i in numbers:
    if i > max_number:
        max_number = i
print("가장 큰 숫자:", max_number)

