# 출력: 없음
# 입력: 주소
not_mine = ['용인시', '둔산동', '번동', '장안구', '온천동', '구로구', '군포시']
address_list = []

while True:
    address = input('주소: ')
    check = False
    for i in not_mine:    # not_mine 리스트에 있는것들 중 하나라도
        if i in address:     # 입력받은 값에 포함되어 있으면
            check = True     # check 변수를 False에서 True로 바꾼다.

    if check:                  # check변수가 True라면,
        continue             # 그 주소는 리스트에 더하지 않고 다시 반복을 시작한다.
    
    address_list += [address]    # check변수가 False라면, 그 주소는 리스트에 더한다.


