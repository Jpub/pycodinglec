# 출력 : 시간대에 맞는 문구
# 입력 : 시각
def day():
    return '그대의 근로는 태양보다도 밝다.'

def night():
    return '아름다운 서울의 야경, 당신은 하나의 별이다.'

time = int(input('현재시각(0~24): '))
if 8 <= time <= 17:
    phrase = day()
else:
    phrase = night()
print(phrase)

