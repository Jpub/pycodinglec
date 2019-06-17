def judge(name, n):
    """참여자의 승패를 판단하는 함수"""
    if n == 31:
        print(name, "패배")
        return True
    else:
        return False

def BR31():
    """참여자의 턴 및 게임의 진행 전반을 관리하는 함수"""
    user_numbers = [0]
    k = 0
    while True:
        k += 1    # 턴을 세는 변수 추가 후 인수로 전달
        computer_numbers = computer_turn(user_numbers, k)
        if judge('컴퓨터', computer_numbers[-1]):  # 컴퓨터의 패배 여부 판단(사실 불필요)
            break
        user_numbers = user_turn()
        if judge('사람', user_numbers[-1]):
            break

def computer_turn(previous_numbers, k):
    """컴퓨터의 턴에 숫자를 결정하고 출력하는 함수. 임의선택이 아닌, 공식에 의한 숫자 선택이 수행된다."""
    last_number = 4*k-2
    numbers = [i for i in range(previous_numbers[-1]+1, last_number+1)]
    # 숫자 결정 완료

    print("컴퓨터: ", end='')
    for i in numbers:
        print(i, end=' ')
    print()
    # 숫자 출력 완료

    return numbers

def user_turn():
    """사용자 턴에 숫자를 입력받아서 이를 처리하는 함수"""
    numbers = [int(i) for i in input("사람: ").split()]
    return numbers

if __name__ == "__main__":
    BR31()
