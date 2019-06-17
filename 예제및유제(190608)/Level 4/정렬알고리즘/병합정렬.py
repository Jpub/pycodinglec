def main():
    numbers = [int(i) for i in input("수열: ").split()]
    merge_sort(numbers)
    print(numbers)

def merge_sort(numbers):
    divide(numbers, 0, len(numbers)-1)

# 분할
def divide(numbers, start, end):
    if start == end:
        return
    mid=int((start+end)/2)
    divide(numbers, start, mid)
    divide(numbers, mid+1, end)
    merge(numbers, start, mid, end)

# 병합
def merge(numbers, start, mid, end):
    sub_list = [None]*(end-start+1)
    first_i = start               # 앞수열의 시작 인덱스
    second_i = mid+1              # 뒷수열의 시작 인덱스
    for i in range(len(sub_list)):
        if first_i == mid+1:
            sub_list[i] = numbers[second_i]
            second_i += 1
        elif second_i == end+1:
            sub_list[i] = numbers[first_i]
            first_i += 1
        else:
            if numbers[first_i] > numbers[second_i]:
                sub_list[i] = numbers[second_i]
                second_i += 1
            else:
                sub_list[i] = numbers[first_i]
                first_i += 1
    numbers[start:end+1] = sub_list[:]

if __name__ == "__main__":
    main()

