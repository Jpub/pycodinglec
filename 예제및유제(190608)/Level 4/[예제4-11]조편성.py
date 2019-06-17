import random
people = input("사람들: ").split()
random.shuffle(people)
n = int(input("그룹 숫자: "))
for i in range(1, n+1):
    print("%d조:" % i, end=' ')
    for j in range(len(people)):
        if j % n+1 == i:
            print(people[j], end=' ')
    print()    # 줄바꿈


