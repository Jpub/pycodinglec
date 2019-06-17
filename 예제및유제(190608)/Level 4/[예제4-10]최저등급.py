with open("판별대상.txt") as file:
    while True:
        student = file.readline()
        if student == '':
            break
        student = student.rstrip('\n').split()
        for i in [1, 2, 3]:
            student[i] = int(student[i])
        condition1 = student[1]+student[2]+student[3] < 10
        condition2_1 = student[2]+student[1] < 8  # 두 과목의 평균이 4 미만이려면
        condition2_2 = student[2]+student[3] < 8  # 합이 8 미만이어야 한다.
        if condition1 and (condition2_1 or condition2_2):
            print(student[0])

