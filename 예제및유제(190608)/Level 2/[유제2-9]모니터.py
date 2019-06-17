# 출력: 정상 또는 비정상
# 입력: 일곱 자리 일련번호
serial_numbers = [1111555, 2223322, 2521249, 8504037]
number = int(input('모니터 일련번호: '))
if number in serial_numbers:
    print('정상')
if number not in serial_numbers:
    print('비정상')


