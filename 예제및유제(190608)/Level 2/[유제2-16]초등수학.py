# 출력: 여러 개의 숫자
# 입력: 없음(스스로 이용할 프로그램)
for i in range(1, 100):
    if i % 2 == 0 or i % 3 == 0 or i % 7 != 0:
        continue
    else:
        print(i)

