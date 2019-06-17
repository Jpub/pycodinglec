n = int(input("자연수: "))
if int(n**0.5) != n**0.5:
    print('자연수인 양의 제곱근이 존재하지 않음')
else:
    print("양의 제곱근:", int(n**0.5))

