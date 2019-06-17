# 출력: 학점(영문 형태의 등급)
# 입력: 0이상 100이하의 시험점수

# 약속(함수 정의)
def get_score():
    score = int(input('점수를 입력하세요: '))
    return score

def grading(score):
    if score >= 98:
        return 'A'
    elif score >= 95:
        return 'B'
    elif score >= 90:
        return 'C'
    else:
        return 'F'

# 명령(함수 호출)
if __name__ == "__main__":
    score = get_score()         # 프로그램 전체의 input
    grade = grading(score)     # 프로그램 전체의 process
    print(grade)              # 프로그램 전체의 output

