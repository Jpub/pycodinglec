position = {'사원', '주임', '대리', '과장', '차장', '부장', '이사', '상무이사', '전무이사', '대표이사', '부사장', '사장'}
name = []
with open("이름1.txt", "r") as file1:
    while True:
        line = file1.readline()
        if line == '':
            break
        line = set(line.rstrip('\n').split())
        name += list(line-position)    # 차집합 연산의 결과를 name 리스트에 추가
    name = set(name)    # name 리스트를 집합으로 형 변환하여 중복 요소를 삭제

with open("이름2.txt", "w") as file2:
    for each_name in name:
        file2.write(each_name+' ')


