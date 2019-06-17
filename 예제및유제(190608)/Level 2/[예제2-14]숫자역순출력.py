# 출력 : 숫자. 입력받은 것과 역순으로.
# 입력 : 숫자의 개수와 여러 가지 숫자.

n = int(input("몇 개?: "))
numbers = []
for i in range(1, n+1):
    x = input("숫자 "+str(i)+": ")
    numbers = numbers+[x]
for i in range(n-1, -1, -1):
    print(numbers[i])


