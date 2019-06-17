coins = [500, 100, 50, 10]    # 동전의 종류
change = int(input("거슬러줄 금액: "))    # change: 거스름돈
count = 0    # 동전의 개수
for each_coin in coins:
    if not change:    # 더 거슬러줄 금액이 없다면 반복 종료
        break
    count += change // each_coin
    change = change % each_coin
print(count)
