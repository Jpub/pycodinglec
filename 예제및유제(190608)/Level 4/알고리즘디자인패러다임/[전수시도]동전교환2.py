result = 0
change = 0
coins = []
max_coins = []

def main():
    global max_coins
    # ①
    get_data()
    
    # ②
    max_coins = [change//i for i in coins]

    # ③, ④
    get_answer(max_coins[:])
    
    print(result)

def get_data():
    global change
    global coins
    change = int(input("거슬러줄 금액: "))
    coins = [int(i) for i in input("동전의 종류: ").split()]

def total_value(combination, coins):    # 동전의 가치 총합을 계산하여 반환
    total = 0
    for i in range(len(coins)):
        total += combination[i]*coins[i]
    return total

def get_answer(combination):
    global result
    while sum(combination):  # combination 리스트가 [0, 0, ..., 0]이 되면 종료
        # ④
        if total_value(combination, coins) == change:
            if not result:
                result = sum(combination)
            else:
                if result > sum(combination):
                    result = sum(combination)
        # ③
        combination[-1] -= 1
        for i in range(len(combination)-1, 0, -1):
            if combination[i] == -1:
                combination[i] = max_coins[i]
                combination[i-1] -= 1        # 받아내림

if __name__ == "__main__":
    main()

#
