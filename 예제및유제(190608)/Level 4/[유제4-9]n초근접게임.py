import time
n = int(input("n: "))
tolerance = 0.1   # 오차허용비율
for count in ['3', '2', '1']:
    print(count, end=', ')
    time.sleep(1)
    
print("시작!", end='')
start = time.time()

input()
end = time.time()

elapsed_time = end-start    # 경과 시간
print("%.2f" % elapsed_time, end=' ')

if abs(elapsed_time-n) < n*tolerance:
    print("성공")
else:
    print("실패")


