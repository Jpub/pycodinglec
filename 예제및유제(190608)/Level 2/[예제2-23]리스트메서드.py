# 입력: 메뉴번호와 각 메뉴에 따른 추가정보
# 출력: 리스트, 메뉴, 사용 안내
list_for_user = []
while True:
    print()
    print(list_for_user)
    print('1: 추가, 2: 삽입, 3: 수정, 4: 삭제, 5: 종료')
    menu = input('무엇을 할 것입니까? : ')
    if menu == '5':
        break
    elif menu == '1':
        new_one = input('어떤 값을 추가하시겠습니까? : ')
        list_for_user.append(new_one)
    elif menu == '2':
        new_one = input('어떤 값을 삽입하시겠습니까? : ')
        order = input('몇 번째로 삽입하시겠습니까? : ')
        list_for_user.insert(int(order)-1, new_one)
    elif menu == '3':
        order = input('몇 번째 값을 수정하시겠습니까? : ')
        modified_one = input('무엇으로 바꾸시겠습니까? : ')
        list_for_user.remove(list_for_user[int(order)-1])
        list_for_user.insert(int(order)-1, modified_one)
    elif menu == '4':
        target = input('어떤 값을 삭제하시겠습니까? : ')
        list_for_user.remove(target)
    else:
        print('다시 입력하세요')

