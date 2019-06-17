n = int(input("자연수: "))
natural_number = False
for i in range(1, n+1):
    if i**2 == n:
        print("양의 제곱근:", i)
        natural_number = True
        break
if not natural_number:
    print('자연수인 양의 제곱근이 존재하지 않음')

