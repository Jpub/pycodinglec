import random
print("[보기] 가위, 바위, 보")
user = input("당신은? ")

computer = random.randint(1, 3) # 1 또는 2 또는 3 중 하나의 정수를 무작위로 선택
if computer == 1:
    computer = '가위'
elif computer == 2:
    computer = '바위'
else:
    computer = '보'
print("저는?", computer)

if user == computer:
    print("우리 비겼네요!")
elif((user == '가위' and computer == '바위')
     or (user == '바위' and computer == '보')
     or (user == '보' and computer == '가위')):
    print("제가 이겼네요!")
else:
    print("제가 졌군요!")

