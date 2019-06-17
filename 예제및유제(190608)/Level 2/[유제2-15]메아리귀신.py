# 출력: 특수문자가 아닌, 입력받은 문자열의 마지막 음절, 또는 히-히히히!
# 입력: 문자열.
while True:
    sentence = input()
    if sentence[-1] == '.' or sentence[-1] == '?':   # 마지막 글자가 특수문자인 경우
        if sentence[-2] == '요':
            print('히-히히히!')
            break
        else:
            print(sentence[-2]+'?')
    else:    # 마지막 글자가 특수문자가 아닐 경우
        if sentence[-1] == '요':
            print('히-히히히!')
            break
        else:
            print(sentence[-1]+'?')


