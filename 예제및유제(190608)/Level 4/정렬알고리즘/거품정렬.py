numbers = [int(i) for i in input("숫자들: ").split()]
for i in range(len(numbers)-1, 0, -1):
    for j in range(i):
        if numbers[j] > numbers[i]:
            #부등호 방향을 바꾸면 내림차순 정렬
            numbers[i], numbers[j] = numbers[j], numbers[i]
print(numbers)
