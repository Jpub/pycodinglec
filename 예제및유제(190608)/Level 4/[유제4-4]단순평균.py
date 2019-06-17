numbers = input("숫자: ")
numbers = [int(i) for i in numbers.split()]
total = 0
for i in numbers:
    total += i
print(total/len(numbers))  # 평균: 숫자의 합계를 숫자의 개수로 나눔

