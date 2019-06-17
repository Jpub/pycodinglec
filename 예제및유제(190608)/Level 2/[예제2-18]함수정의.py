# 출력: 직사각형 넓이
# 입력: 직사각형 가로, 세로
def rectangle(x, y):
    return x*y

a = int(input('가로 길이 : '))
b = int(input('세로 길이 : '))
s = str(rectangle(a, b))
print('넓이는', s+'입니다')

