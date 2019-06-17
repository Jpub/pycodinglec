contest_result = open("노래경연결과.txt", "r")
contest_entry = open("경연참여자.txt", "w")
while True:
    line = contest_result.readline()
    if not line:
        break
    
    for i in range(len(line)-1, -1, -1):    # 한 줄을 뒤에서부터 읽어
        if line[i] == ' ':    # 첫 공백을 찾은 뒤
            contest_entry.write(line[:i]+'\n')    # 그 지점 전까지만 출력하도록 한다.
            break
        
contest_entry.close()
contest_result.close()


