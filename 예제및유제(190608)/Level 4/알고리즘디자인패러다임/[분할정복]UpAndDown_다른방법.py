def binary_search(left, right):
    while True:
        if left == right:
            return right
        middle = int((left+right)/2)    # 중앙값
        menu = input("당신의 숫자는 "+str(middle)+"입니까?: ")
        if menu == '3':
            return middle
        elif menu == '1':
            left = middle+1
        else:
            right = middle-1

