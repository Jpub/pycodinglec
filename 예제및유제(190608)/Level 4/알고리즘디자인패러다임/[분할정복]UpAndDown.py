def binary_search(left, right):
    if left == right:
        return right
    mid = int((left+right)/2)
    menu = input("당신의 숫자는 "+str(mid)+"입니까?: ")
    if menu == '3':
        return mid
    elif menu == '1':
        return binary_search(mid+1, right)
    else:
        return binary_search(left, mid-1)

print("""[보기]
1. Up
2. Down
3. Yes""")
left_boundary = 1    # 좌측(작은 쪽)경계
right_boundary = 100    # 우측(큰 쪽)경계
print("당신의 숫자는", str(binary_search(left_boundary, right_boundary))+"입니다")

