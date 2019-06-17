# 출력: 가장 작은 숫자
# 입력: 숫자 여러 개

numbers = input("여러 개의 숫자 입력: ")
numbers = [int(i) for i in numbers.split()]
min_number = numbers[0]
for i in numbers:
    if i < min_number:
        min_number = i
print("가장 작은 숫자:", min_number)

