n = int(input("몇 개?: "))
numbers = []
i = 1
while i <= n:
    x = input("숫자 "+str(i)+": ")
    numbers = numbers+[x]
    i = i+1
i = n-1
while i >= 0:
    print(numbers[i])
    i = i - 1
