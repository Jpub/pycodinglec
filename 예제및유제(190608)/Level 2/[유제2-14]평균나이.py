# 출력 : 평균 나이
# 입력 : 사람 수, 각 사람의 나이

n = int(input("몇 명?: "))
age_sum = 0
for i in range(1, n+1):
    age = int(input("학생 "+str(i)+": "))
    age_sum = age_sum+age
print("평균: ", age_sum/n)




