contest_result = open("노래경연결과.txt", "r")
score_sum = 0    # 점수 합계
count = 0    # 사람 숫자
while True:
    line = contest_result.readline()
    if not line:
        break
    score_sum += int(line.split()[-1].rstrip('\n'))
    count = count + 1
print("참가자 평균점수 :", score_sum/count)
contest_result.close()


