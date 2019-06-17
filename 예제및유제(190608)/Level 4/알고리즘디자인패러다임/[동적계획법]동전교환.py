memoization = dict()    # 딕셔너리를 이용한 메모이제이션 적용
def get_answer(n):
    if n in coins:  # 베이스 케이스: 동전 액면과 같은 금액
        memoization[n] = 1
        return 1
    available_count = []
    for i in coins:
        if n-i > 0:
            memo = memoization.get(n-i)
            # memo가 없으면 메서드 get은 None을 반환함
            if memo:
                available_count.append(memo)
            else:
                available_count.append(get_answer(n-i))
    memoization[n] = min(available_count)+1
    return memoization[n]

change = int(input("거슬러줄 금액: "))
coins = [int(i) for i in input("동전의 종류: ").split()]
print(get_answer(change))

#####################
