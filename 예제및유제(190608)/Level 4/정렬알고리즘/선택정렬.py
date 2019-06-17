numbers = [int(i) for i in input("수열: ").split()]
for i in range(len(numbers)-1):
    min_i = i
    for j in range(i+1, len(numbers)):
        if numbers[min_i] > numbers[j]:  # 부등호 방향을 바꾸면 내림차순 정렬
            min_i = j
    numbers[i], numbers[min_i] = numbers[min_i], numbers[i]
print(numbers)
