result = {'S': 0, 'A': 0, 'B': 0, 'C': 0}

def deduction(a, b):    # 감점 총합을 계산하여 반환하는 함수
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2] + a[3]*b[3]

with open("테스트.txt") as file:
    while True:
        record = file.readline()
        if record == '':
            break
        record = record.rstrip('\n').split()

        for i, value in enumerate(record):
            record[i] = int(value)    # 점수를 계산하기 위해, 문자열에서 정수로 형 변환

        penalty_point = [2, 6, 4, 10]    # 감점기준

        score = 100-deduction(penalty_point, record)
        
        if score >= 90:
            result['S'] += 1        # 등급 산출 후 해당 등급 인원을 1 상승시킴
        elif score >= 80:
            result['A'] += 1
        elif score >= 60:
            result['B'] += 1
        else:
            result['C'] += 1
        
for key, value in result.items():
    print(key, value)
