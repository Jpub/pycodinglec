# 출력: 학점(영문 형태의 등급)
# 입력: 0이상 100이하의 시험점수
score = int(input('점수를 입력하세요: '))
if score >= 98:
    print('A')
elif score >= 95:
    print('B')
elif score >= 90:
    print('C')
else:
    print('F')

