# 출력: '환영합니다, 관리자님!' 또는 '등록되지 않은 사용자입니다.'
# 입력: ID와 PW
ID = input('ID를 입력하세요: ')
PW = input('PW를 입력하세요: ')
if ID == 'admin' and PW == '1234':
    print('환영합니다, 관리자님!')
else:
    print('등록되지 않은 사용자입니다.')

