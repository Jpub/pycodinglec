import random

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
    while True:
        computer_numbers = computer_turn(user_numbers)
        if judge('컴퓨터', computer_numbers[-1]):
            break
        user_numbers = user_turn()
        if judge('사람', user_numbers[-1]):
            break

def computer_turn(previous_numbers):
    """컴퓨터의 턴에 숫자를 결정하고 출력하는 함수"""
    last_number = random.randint(previous_numbers[-1]+1, previous_numbers[-1]+3)
    if last_number >= 31:
        last_number = 31
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



