numbers = [int(i) for i in input("수열: ").split()]
for i in range(len(numbers)-1):
    min_i = numbers.index(min(numbers[i:]), i)    # min을 max로 바꾸면 내림차순 정렬
    numbers[i], numbers[min_i] = numbers[min_i], numbers[i]
print(numbers)
