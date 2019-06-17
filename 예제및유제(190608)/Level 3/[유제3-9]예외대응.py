# 출력: 구구단 중 한 단
# 입력: 단 수
file = open("구구단출력.txt", "w")
try:
    n = int(input("몇 단?: "))
except Exception as e:
    file.write(str(e))
else:
    for i in range(1, 10):
        file.write(str(n)+" x "+str(i)+" = "+str(n*i)+"\n")
finally:
    file.close()
