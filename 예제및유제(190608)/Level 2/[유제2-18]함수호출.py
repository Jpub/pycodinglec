# 출력 : 삼각형 넓이
# 입력 : 삼각형의 밑변과 높이
def triangle(b, h):
    return 0.5*b*h

x = int(input('밑변: '))
y = int(input('높이: '))
s = triangle(x, y)
print('넓이는', str(s)+'입니다')


#

