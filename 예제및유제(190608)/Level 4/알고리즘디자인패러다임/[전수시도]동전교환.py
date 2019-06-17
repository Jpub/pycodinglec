change = int(input("거슬러줄 금액: "))

available_answer=[]    # 정답 후보
for i1 in range(change//500+1):
    for i2 in range(change//100+1):
        for i3 in range(change//50+1):
            for i4 in range(change//10+1):
                if i1*500+i2*100+i3*50+i4*10 == change:
                    available_answer.append(i1+i2+i3+i4)
print(min(available_answer))
