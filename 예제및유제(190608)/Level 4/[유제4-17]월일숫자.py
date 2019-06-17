def judge(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False  # 한 번이라도 나눠떨어지면 False를 반환
    return True    # 그렇지 않으면 True를 반환

days=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
월일숫자 = []
for i in range(12):
    for j in range(1, days[i]+1):
        월일숫자.append(int(str(i+1)+str(j)))
월일숫자 = set(월일숫자)  # 중복제거. 12월 1일이나 1월 21일 모두 121이다.
for i in 월일숫자:
    if judge(i):
        print(i)

