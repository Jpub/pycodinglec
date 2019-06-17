numbers = [int(i) for i in input("수열: ").split()]
for i in range(1, len(numbers)):
    for j in range(i-1, -1, -1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
        else:
            break
print(numbers)
