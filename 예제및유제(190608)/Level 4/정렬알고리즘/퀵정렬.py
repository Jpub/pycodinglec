def main():
    numbers = [int(i) for i in input("수열: ").split()]
    quick_sort(numbers)
    print(numbers)

def quick_sort(numbers):
    quick(numbers, 0, len(numbers)-1)

def quick(numbers, start, end):
    if end-start <= 0:
        return
    pivot_i = start    # pivot_i: 기준값의 인덱스
    for i in range(start+1, end+1):
        if numbers[i] < numbers[pivot_i]:
            numbers.insert(pivot_i, numbers.pop(i))
            pivot_i += 1
    quick(numbers, start, pivot_i-1)
    quick(numbers, pivot_i+1, end)
    
if __name__ == "__main__":
    main()
